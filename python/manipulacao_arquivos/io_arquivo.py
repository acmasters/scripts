#! /usr/bin/python3

arquivo = open('pessoa.csv')

dados = arquivo.read()

arquivo.close()

for registro in dados.splitlines():
    print ('Nome: {}, Idade: {}'.format(*registro.split(',')))