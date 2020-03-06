#! /usr/bin/python3

arquivo = open('pessoa.csv')

for registro in arquivo:
    print ('Nome: {}, Idade: {}'.format(*registro.split(',')))
arquivo.close()
