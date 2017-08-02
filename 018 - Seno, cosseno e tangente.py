# Faça um programa que leia um angulo qualquer e mostre na tela
# o  valor do seno, cosseno e tangente desse angulo

import math

ang = float(input('Digite um ângulo: '))

print('O seno: {:.2f}'.format(math.sin(math.radians(ang))))
print('O cosseno: {:.2f}'.format(math.cos(math.radians(ang))))
print('A tangente: {:.2f}'.format(math.tan(math.radians(ang))))
