# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triangulo retangulo
# calcule e mostre o comprimento da hipotenusa.

import math

c1 = float(input('Cateto oposto: '))
c2 = float(input('Cateto adjacente: '))

hipo = (math.pow(c1, 2) + math.pow(c2, 2))
hipo = math.sqrt(hipo)

print('Hipotenusa = {}'.format(hipo))
