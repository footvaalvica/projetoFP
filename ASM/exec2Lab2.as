ORIG            4000h
                
X               WORD    5
Y               WORD    6
Z               WORD    7

ORIG            0000h

                MVI     R5, X
                LOAD    R2, M[R5]
                
                MVI     R5,Y
                LOAD    R3, M[R5]
                
                MVI     R5, Z
                LOAD    R4, M[R5]
                
                ADD     R1,R2,R3
                ADD     R1,R1,R4
                
Fim:            BR      Fim