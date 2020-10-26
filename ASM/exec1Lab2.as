X               EQU     5
Y               EQU     3

ORIG            4000h

A               WORD    10
B               WORD    7
C               WORD    3

ORIG            0000h

                MVI     R3,B
                LOAD    R2,M[R3]
                MVI     R3,Y
                
                INC     R2
                SUB     R2,R2,R3
                ADD     R2,R2,R2
                
                MVI     R3,B
                STOR    M[R3],R2

                MVI     R3,A
                LOAD    R2,M[R3]
                MVI     R1,X 
                
                DEC     R2
                DEC     R2
                ADD     R2,R2,R1
                ADD     R2,R2,R2
                ADD     R2,R2,R2
                ADD     R2,R2,R2
                
                MVI     R3,A
                STOR    M[R3],R2
                
                MVI     R3,A
                LOAD    R1,M[R3]
                
                MVI     R3,B
                LOAD    R2,M[R3]
                
                ADD     R3,R1,R2
                
                MVI     R1, C
                STOR    M[R1], R3
                
Fim:            BR      Fim