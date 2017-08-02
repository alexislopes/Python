# Crie um programa que leia um numero real qualquer
#pelo teclado e mostre na tela a sua porção inteira

#EX: Digeite um númmero: 6.127
# o numero 6.127 tem a porção inteira 6.

import math

num = float(input('Digite um número: '))
print('O número {} tem a porção inteira {}'.format(num, math.floor(num)))
