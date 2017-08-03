# O mesmo professor do desafio anterior quer sortear
# a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.

import random

lista=[]
cont = 0

while cont < 4:
    nome = input('Digite os nomes: ')
    lista.append(nome)
    cont += 1

print('A orderm será:\n{}'.format(sorted(lista)))
