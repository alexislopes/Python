# Crie um programa que leia algo pelo teclado e mostre na tela
# seu tipo primitivo e todas as informações possiveis sobre ela.

i = input('Digite algo: ')

print('O tipo primitivo de {} é: '.format(i), type(i))
print('{} só tem espaços? '.format(i), i.isspace())
print('{} é numérico? '.format(i), i.isnumeric())
print('{} é afabético? '.format(i), i.isalpha())
print('{} é alfanumérico? '.format(i), i.isalnum())
print('{} está em maiúsculas? '.format(i), i.isupper())
print('{} está em minúsculas? '.format(i), i.islower())
print('{} está capitalizada? '.format(i), i.istitle())
