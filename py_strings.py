#!/usr/bin/python3

def make_pi():
     q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
     for j in range(1000):
          if 4 * q + r - t  < m * t:
               yield m  
               q, r, t, k, m, x =  10*q , 10*(r-m*t), t, k, (10*(3*q+r))//t -10*m, x
          else:
               q, r, t, k, m, x =  q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2

digits =  make_pi()

pi_list = []
my_array = []

for i in make_pi():
     my_array.append(str(i))

my_array =  my_array[:1] + ['.'] + my_array[1:]

#Gera o valor de pi extenso
big_string = "".join(my_array)

pi_string = "pi_completo.txt"

with open(pi_string, 'w') as file_object: 
     file_object.write(big_string)

     birthday = input("Digite o dia do seu aniversario, no formato mmddyy: ")
     if birthday in pi_string:
          print("Seu Aniversario aparece na string do pi completo")
     else:
         print("Infelizmente seu aniversario nao aparece no pi completo")






