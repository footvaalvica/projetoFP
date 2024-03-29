STACKBASE       EQU     8000h
                ORIG    0000h
                MVI     R6, STACKBASE
                
                MVI     R1, 10
                JAL     Base   
                
Fim:            BR      Fim

Base:           MVI     R2,1
                CMP     R1,R2
                BR.P    Recursao
                ADD     R3,R3,R1
                JMP     R7
                
Recursao:       DEC     R1
                STOR M[R6], R7
                DEC R6
                STOR M[R6], R1
                DEC R6
                
                JAL     Base ; recursive call
                
                INC R6
                LOAD R1, M[R6]
                INC R6
                LOAD R7, M[R6]
                
                STOR M[R6], R7
                DEC R6
                STOR M[R6], R1
                DEC R6
                
                DEC     R1 ; argument is now n-2
                JAL     Base ; recursive call
                
                INC R6
                LOAD R1, M[R6]
                INC R6
                LOAD R7, M[R6]

                JMP     R7
