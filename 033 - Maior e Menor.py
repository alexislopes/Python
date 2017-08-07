# Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print('Maior {}'.format(n1))
    print('Menor {}'.format(n2) if n2 < n3 else 'Menor {}'.format(n3))

if n2 > n3 and n2 > n1:
    print('Maior {}'.format(n2))
    print('Menor {}'.format(n3) if n3 < n1 else 'Menor {}'.format(n1))

if n3 > n2 and n3 > n1:
    print('Maior {}'.format(n3))
    print('Menor {}'.format(n2) if n2 < n1 else 'Menor {}'.format(n1))
