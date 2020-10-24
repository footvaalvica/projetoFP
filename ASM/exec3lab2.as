TRINTA          EQU     30
DEZ             EQU     10

ORIG            4000h

X               WORD    9
M               WORD    8
N               WORD    22

ORIG            0000h

                MVI     R6,N
                LOAD    R2,M[R6]
                MVI     R1,DEZ
                
                
                ADD     R2,R2,R2
                ADD     R2,R2,R1
                
                MVI     R6,M
                LOAD    R4,M[R6]
                MVI     R1,TRINTA
                
                SUB     R4,R1,R4
                
                ADD     R3,R4,R2
                
                MVI     R6,X
                STOR    M[R6],R3
                
Fim:            BR      Fim