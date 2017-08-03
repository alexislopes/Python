# Crie um programa que leia o nome completo de uma pessoa e mostre

# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = input('Digite algum nome: ')

print(nome.upper())
print(nome.lower())
nome = nome.split()
print('O primeiro nome tem {} letras'.format(len(nome[0])))
nome = ''.join(nome)
print('O nome tem {} letras'.format(len(nome)))
