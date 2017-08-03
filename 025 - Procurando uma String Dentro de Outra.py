# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem 'SILVA' no nome.

nome = input('Digite um Nome: ').lower().split()
nome = nome.count('silva')

if nome > 0:
    print('Sim, é da família Silva.')
else:
    print('Não é da família Silva.')
