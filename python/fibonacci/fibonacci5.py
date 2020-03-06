#! /usr/bin/python3
# 0,1,2,3,5,8,13,21
#Exemplo usando Regra Fibonacci v2

def fibonacci(limite):
    resultado = [0, 1]
    while  resultado[-1] < limite: 
        resultado.append(sum(resultado[-2:]))
    return resultado

if __name__ == "__main__":
    for fib in fibonacci(1000):
        print(fib)
