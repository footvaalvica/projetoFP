STACKBASE       EQU     8000h
                ORIG    0000h
                MVI     R6, STACKBASE
                
                ;a soma dos n primeiros termos é igual a
                ;fibonacci(n+2) - 1
                
                MVI     R1, 10
                INC     R1
                INC     R1
                JAL     Base   
                
                DEC     R3
                
Fim:            BR      Fim

Base:           MVI     R2,1
                CMP     R1,R2
                BR.P    Recursao
                ADD     R3,R3,R1
                JMP     R7
                
Recursao:       DEC     R1
                PUSH    R7
                PUSH    R1
                
                JAL     Base ; recursive call
                
                POP     R1
                POP     R7
                
                PUSH    R7
                PUSH    R1
                
                DEC     R1 ; argument is now n-2
                JAL     Base ; recursive call
                
                POP     R1
                POP     R7

                JMP     R7
