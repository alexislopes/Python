# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o ultimo nome separadamente.

# EX: Ana Maria de Souza.
# Primeiro: Ana. último: Souza

nome = input('Digite um nome: ').split()
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[-1]))
