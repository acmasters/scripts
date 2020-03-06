#! /usr/bin/python3

with open('pessoa.csv') as arquivo:
    for registro in arquivo:
        print ('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo já finalizado !!')
