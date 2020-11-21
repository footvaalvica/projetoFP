;=================================================================
; CONSTANTS
;-----------------------------------------------------------------
; Text window
TERM_READ       EQU     FFFFh	; read characters
TERM_WRITE      EQU     FFFEh	; write characters
TERM_STATUS     EQU     FFFDh	; status (0-no key pressed; 1-key pressed)
TERM_CURSOR     EQU     FFFCh	; position the cursor
TERM_COLOR      EQU     FFFBh	; change the colors
; leds & LCD
LCD_WRITE       EQU     FFF5h	; write on LCD
LCD_CURSOR      EQU     FFF4h	; position LCD cursor
; Stack
SP_INIT         EQU     7000h	; initial stack location
                OPT     ASCII

;=================================================================
; GLOBAL VARIABLES
;-----------------------------------------------------------------
                ORIG    0
LCD_NUMS        TAB     4

;=================================================================
; MAIN: the starting point of your program
;-----------------------------------------------------------------
                ORIG    0
				; initialize the stack pointer
MAIN:           MVI     R6,SP_INIT

				; wait for a key to be pressed
                MVI     R4,TERM_STATUS
.LOOP:          LOAD    R1,M[R4]		; read the terminal status
                CMP     R1,R0
                JAL.NZ  PROCESS_CHAR	; call process_char when a key is pressed
                BR      .LOOP


;=================================================================
; PROCESS_CHAR: function that process characters on text window
;-----------------------------------------------------------------
PROCESS_CHAR:   ; SAVE CONTEXT
                DEC     R6
                STOR    M[R6],R7
                ; ECHO CHARACTER FROM TERMINAL
                MVI     R1,TERM_READ
                LOAD    R2,M[R1]
                MVI     R1,TERM_WRITE
                STOR    M[R1],R2
				; ----------------------
				; Exercise 2a
				; ----------------------
                ; VERIFY IF IT IS A DIGIT...
                
                MVI     R1,'>'
                PUSH    R5
                CMP     R2,R1
                JAL.Z   SHIFTRIGHT
                POP     R5
                MVI     R1,'<'
                PUSH    R5
                CMP     R2,R1
                JAL.Z   SHIFTLEFT
                POP     R5
                MVI     R1,'9'
                CMP     R2,R1
                BR.P    .RETURN         ; if key>'9' go out
                MVI     R1,'0'
                CMP     R2,R1           ; if key<'0' go out
                BR.N    .RETURN
                ; ... WRITE ON LEDS
                SUB     R2,R2,R1        ; convert from ascii to number
                MOV     R5,R2
				; ----------------------
				; Exercise 2b&2c
				; ----------------------
                ; ... SAVE VALUE ON STACK
                DEC     R6
                STOR    M[R6],R2
                ; RETRIEVE SAVED VALUE
                LOAD    R1,M[R6]
                INC     R6
                JAL     WRITE_ON_LCD
                ; RELOAD CONTEXT & EXIT
                LOAD    R7,M[R6]
                INC     R6
.RETURN:        JMP     R7

SHIFTRIGHT:     SHRA    R5
                MOV     R1,0Eh
                JAL     WRITE_ON_LCD
                MOV     R1,0Dh
                JAL     WRITE_ON_LCD
                MOV     R1,R5
                JAL     WRITE_ON_LCD
                ; RELOAD CONTEXT & EXIT
                LOAD    R7,M[R6]
                INC     R6
                BR      MAIN.LOOP
                
SHIFTLEFT:      SHLA    R5
                MOV     R1,0Ch
                JAL     WRITE_ON_LCD
                MOV     R1,0Dh
                JAL     WRITE_ON_LCD
                MOV     R1,R5
                JAL     WRITE_ON_LCD
                ; RELOAD CONTEXT & EXIT
                LOAD    R7,M[R6]
                INC     R6
                BR      MAIN.LOOP

;=================================================================
; WRITE_ON_LCD: writes a value on LCD, rotating the remaining 
;               16 digits previously written
;-----------------------------------------------------------------
WRITE_ON_LCD:   ; SAVE CONTEXT
                DEC     R6
                STOR    M[R6],R5

                ; POSITION CURSOR
                MVI     R2, LCD_CURSOR
                MVI     R3, 8000h
                STOR    M[R2],R3
				
                ; CONVERT INPUT DIGIT TO CHAR
                MVI     R2,'0'
                ADD     R1,R1,R2
                ; LOAD BASE ADDRESS
                MVI     R3, LCD_NUMS

                MVI     R5,4
.LOOP:          ; INSERT VALUE
                MVI     R2, LCD_WRITE
                STOR    M[R2],R1
                LOAD    R2, M[R3]
                STOR    M[R3],R1
                ; GO TO NEXT
                MOV     R1,R2
                INC     R3
				; LOOP
                DEC     R5
                BR.P    .LOOP
                
                
                ; RESTORE CONTEXT AND EXIT
                LOAD    R5,M[R6]
                INC     R6
                
                JMP     R7
