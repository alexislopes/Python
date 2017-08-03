# Um professor quer sortear um dos seus quatro alunos para apagar o quadro
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

lista = []
cont = 0
while cont < 4:
    nome = input('Digite os nomes: ')
    lista.append(nome)
    cont += 1

print('{} vai apagar o quadro.'.format(random.choice(lista)))
