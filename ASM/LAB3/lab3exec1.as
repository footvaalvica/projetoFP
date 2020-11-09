STACKBASE       EQU     8000h
                
                ORIG    4000H
X               STR     'ABCDE',0
Y               STR     '12345',0

                ORIG    5000H
Z               STR     0

                ORIG    0000H
                MVI     R6,STACKBASE                
                
                MVI     R1,X
                MVI     R2,Y

                MVI     R4,Z
                STOR    M[R6], R4
                DEC     R6
                
                JAL     STRCAT
                
Fim:            BR      Fim                

STRCAT:         LOAD    R5, M[R1]
                CMP     R5,R0
                JAL.P   Loopity
                
dois:           LOAD    R5, M[R2]
                CMP     R5,R0
                JAL.P   Loopity2
                
                MVI     R5,Z
                SUB     R5,R4,R5
                
                STOR    M[R6], R5
                DEC     R6
                
                INC     R6
                LOAD    R5, M[R6]
                
                BR      Fim

Loopity:        INC     R6
                LOAD    R4, M[R6]
                STOR    M[R4], R5
                INC     R1
                INC     R4
                STOR    M[R6], R4
                DEC     R6
                CMP     R5,R0
                JMP.P   STRCAT
                JMP     R7
                
Loopity2:       INC     R6
                LOAD    R4, M[R6]
                STOR    M[R4], R5
                INC     R2
                INC     R4
                STOR    M[R6], R4
                DEC     R6
                CMP     R5,R0
                JMP.P   dois
                JMP     R7