;=================================================================
; CONSTANTS
;-----------------------------------------------------------------
; Text window
TERM_READ       EQU     FFFFh
TERM_WRITE      EQU     FFFEh
TERM_STATUS     EQU     FFFDh
TERM_CURSOR     EQU     FFFCh
TERM_COLOR      EQU     FFFBh
; leds
LEDS            EQU     FFF8h
; 7 segment display
DISP7_D0        EQU     FFF0h
DISP7_D1        EQU     FFF1h
DISP7_D2        EQU     FFF2h
DISP7_D3        EQU     FFF3h
DISP7_D4        EQU     FFEEh
DISP7_D5        EQU     FFEFh
; Stack
SP_INIT         EQU     7000h
; timer
TIMER_CONTROL   EQU     FFF7h
TIMER_COUNTER   EQU     FFF6h
TIMER_SETSTART  EQU     1
TIMER_SETSTOP   EQU     0
TIMERCOUNT_MAX  EQU     20
TIMERCOUNT_MIN  EQU     1
TIMERCOUNT_INIT EQU     10
; Switches
SWITCHES        EQU     FFF9h
; interruptions
INT_MASK        EQU     FFFAh
INT_MASK_VAL    EQU     80FFh ; 1000 0000 0001 1010 b

;=================================================================
; Program global variables
;-----------------------------------------------------------------
                ORIG    0
TIMER_COUNTVAL  WORD    10 ; states the current counting period
TIMER_TICK      WORD    0               ; indicates the number of unattended
                                        ; timer interruptions
TIME            WORD    0               ; time elapsed

COUNT_DOWN      WORD    1
;=================================================================
; MAIN: the starting point of your program
;-----------------------------------------------------------------
                ORIG    0
MAIN:           MVI     R6,SP_INIT
                
                ; CONFIGURE TIMER ROUNTINES
                ; interrupt mask
                MVI     R1,INT_MASK
                MVI     R2,INT_MASK_VAL
                STOR    M[R1],R2
                ; enable interruptions
                ENI

                ; START TIMER
                MVI     R2,TIMERCOUNT_INIT
                MVI     R1,TIMER_COUNTER
                STOR    M[R1],R2          ; set timer to count 10x100ms
                MVI     R1,TIMER_TICK
                STOR    M[R1],R0          ; clear all timer ticks
                MVI     R1,TIMER_CONTROL
                MVI     R2,TIMER_SETSTART
                STOR    M[R1],R2          ; start timer
                
                ; WAIT FOR EVENT (TIMER/KEY)
                MVI     R4,TERM_STATUS
                MVI     R5,TIMER_TICK
.LOOP:          LOAD    R1,M[R4]
                CMP     R1,R0
                JAL.NZ  PROCESS_CHAR
                LOAD    R1,M[R5]
                CMP     R1,R0
                JAL.NZ  PROCESS_TIMER_EVENT
                BR      .LOOP


;=================================================================
; PROCESS_CHAR: function that process characters on text window
;-----------------------------------------------------------------
PROCESS_CHAR:   ; ECHO CHARACTER FROM TERMINAL
                MVI     R1,TERM_READ
                LOAD    R2,M[R1]
                MVI     R1,TERM_WRITE
                STOR    M[R1],R2
                ; IF DIGIT...
                MVI     R1,'9'
                CMP     R2,R1
                BR.P    .RETURN
                MVI     R1,'0'
                SUB     R2,R2,R1
                BR.N    .RETURN
                ; ... WRITE ON LEDS
                MVI     R3,LEDS
                STOR    M[R3],R2
.RETURN:        JMP     R7

;=================================================================
; PROCESS_TIMER_EVENT: processes events from the timer
;-----------------------------------------------------------------
PROCESS_TIMER_EVENT:
                ; DEC TIMER_TICK
                MVI     R2,TIMER_TICK
                DSI     ; critical region: if an interruption occurs, value might become wrong
                LOAD    R1,M[R2]
                DEC     R1
                STOR    M[R2],R1
                ENI
                ; IGNORE EVENT (AND EXIT) IF SWITCH 0 IS CLEAR
                MVI     R2,SWITCHES
                LOAD    R1,M[R2]
                MVI     R2,1
                TEST    R1,R2
                BR.NZ   NOTZEROHELP
                DEC R6
                STOR M[R6], R5
                DEC R6
                STOR M[R6], R4
                MVI     R5,TIMER_COUNTVAL
                MVI     R4,10
                STOR    M[R5],R4
                LOAD R4, M[R6]
                INC R6
                LOAD R5, M[R6]
                INC R6
.TIME:          ; UPDATE TIME
                MVI     R1,TIME
                LOAD    R2,M[R1]
                INC     R2
                STOR    M[R1],R2
                ; SHOW TIME ON DISP7_D0
                MVI     R3,fh
                AND     R3,R2,R3
                MVI     R1,DISP7_D0
                STOR    M[R1],R3
                ; SHOW TIME ON DISP7_D1
                SHR     R2
                SHR     R2
                SHR     R2
                SHR     R2
                MVI     R3,fh
                AND     R3,R2,R3
                MVI     R1,DISP7_D1
                STOR    M[R1],R3
                ; SHOW TIME ON DISP7_D2
                SHR     R2
                SHR     R2
                SHR     R2
                SHR     R2
                MVI     R3,fh
                AND     R3,R2,R3
                MVI     R1,DISP7_D2
                STOR    M[R1],R3
                ; SHOW TIME ON DISP7_D3
                SHR     R2
                SHR     R2
                SHR     R2
                SHR     R2
                MVI     R3,fh
                AND     R3,R2,R3
                MVI     R1,DISP7_D3
                STOR    M[R1],R3
                
                JMP     R7

NOTZEROHELP:    DEC R6
                STOR M[R6], R5
                DEC R6
                STOR M[R6], R4
                MVI     R5,TIMER_COUNTVAL
                MVI     R4,20
                STOR    M[R5],R4
                LOAD R4, M[R6]
                INC R6
                LOAD R5, M[R6]
                INC R6
                BR      PROCESS_TIMER_EVENT.TIME
                
;*****************************************************************
; AUXILIARY INTERRUPT SERVICE ROUTINES
;*****************************************************************
AUX_SETNIG:     DEC R6
                STOR M[R6], R5
                DEC R6
                STOR M[R6], R4
                MVI     R5,COUNT_DOWN
                MVI     R4,-1
                STOR    M[R5],R4
                LOAD R4, M[R6]
                INC R6
                LOAD R5, M[R6]
                INC R6

AUX_TIMER_ISR:  ; SAVE CONTEXT
                DEC     R6
                STOR    M[R6],R1
                DEC     R6
                STOR    M[R6],R2
                ; RESTART TIMER
                MVI     R1,TIMER_COUNTVAL
                LOAD    R2,M[R1]
                MVI     R1,TIMER_COUNTER
                STOR    M[R1],R2          ; set timer to count value
                MVI     R1,TIMER_CONTROL
                MVI     R2,TIMER_SETSTART
                STOR    M[R1],R2          ; start timer
                ; I DON'T BELIVE IN TIME
                MVI     R2,TIMER_TICK
                LOAD    R1,M[R2]
                DEC R6
                STOR M[R6], R5
                DEC R6
                STOR M[R6], R4
                MVI     R5,COUNT_DOWN
                LOAD    R4,M[R5]
                ADD     R1,R1,R4
                LOAD R4, M[R6]
                INC R6
                LOAD R5, M[R6]
                INC R6
                STOR    M[R2],R1
                ; RESTORE CONTEXT
                LOAD    R2,M[R6]
                INC     R6
                LOAD    R1,M[R6]
                INC     R6
                JMP     R7

AUX_KEYUPDOWN:  ; SAVE CONTEXT
                DEC     R6
                STOR    M[R6],R2
                DEC     R6
                STOR    M[R6],R3
                ; INCREMENT/DECREMENT BASED ON R1
                MVI     R2,TIMER_COUNTVAL
                LOAD    R3,M[R2]
                CMP     R1,R0
                BR.NZ   .KEYUP
.KEYDOWN:       MVI     R1,TIMERCOUNT_MAX
                CMP     R1,R3
                BR.Z    .SKIPANDEXIT
                INC     R3
                BR      .SAVEANDEXIT
.KEYUP:         MVI     R1,TIMERCOUNT_MIN
                CMP     R1,R3
                BR.Z    .SKIPANDEXIT
                DEC     R3
.SAVEANDEXIT:   STOR    M[R2],R3
                ; RESTORE CONTEXT
.SKIPANDEXIT:   LOAD    R3,M[R6]
                INC     R6
                LOAD    R2,M[R6]
                INC     R6
                JMP     R7

;*****************************************************************
; INTERRUPT SERVICE ROUTINES
;*****************************************************************
                ORIG    7FF0h
TIMER_ISR:      ; SAVE CONTEXT
                DEC     R6
                STOR    M[R6],R7
                ; CALL AUXILIARY FUNCTION
                JAL     AUX_TIMER_ISR
                ; RESTORE CONTEXT
                LOAD    R7,M[R6]
                INC     R6
                RTI
                
                ORIG    7F00H
KEYZERO:        ;SAVE CONTEXTO
                DEC     R6
                STOR    M[R6],R1
                DEC     R6
                STOR    M[R6],R2
                ;MUDAR  VARIAVEL PARA -1
                JAL     AUX_SETNIG
                ; RESTORE CONTEXT
                LOAD    R2,M[R6]
                INC     R6
                LOAD    R1,M[R6]
                INC     R6
                RTI
                
                ORIG    7F10h
KEYONE:         ; SAVE CONTEXT
                DEC     R6
                STOR    M[R6],R1
                DEC     R6
                STOR    M[R6],R2
                ;MUDAR  VARIAVEL
                DEC R6
                STOR M[R6], R5
                DEC R6
                STOR M[R6], R4
                MVI     R5,COUNT_DOWN
                MVI     R4,1
                STOR    M[R5],R4
                LOAD R4, M[R6]
                INC R6
                LOAD R5, M[R6]
                INC R6
                ; RESTORE CONTEXT
                LOAD    R2,M[R6]
                INC     R6
                LOAD    R1,M[R6]
                INC     R6
                RTI