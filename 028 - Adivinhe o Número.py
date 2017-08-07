# escreva um programa que faça o computador 'pensar', entre um numero inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número  escolhido pelo computador

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = random.randint(0, 5)
chute = int(input('Digite um número de 0 a 5: '))

print('Acertô Mizeravi' if chute == num else 'Erroou')
