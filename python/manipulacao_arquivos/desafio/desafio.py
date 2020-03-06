#! /usr/bin/python3
# -*- coding: iso_8859_1 -*-

import csv

with open('desafio-ibge.csv', encoding='iso_8859_1') as dados:
    for dado in csv.reader(dados):
        print('Cidade: {8} , Nome_destinatario {3}'.format(*dado))
    