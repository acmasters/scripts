#! /usr/bin/python3
# 0,1,2,3,5,8,13,21
#Exemplo usando Regra Fibonacci v6

def fibonacci(quantidade, sequencia=(0,1)):
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia +(sum(sequencia[-2:]),))
    
if __name__ == "__main__":
    for fib in fibonacci(10):
        print(fib)
