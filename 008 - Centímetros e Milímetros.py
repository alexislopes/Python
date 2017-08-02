# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetro

metros = float(input('Digite a qauntidade em metros: '))

cm = metros * 100
mm = metros * 1000

print('{} metros em centimetros é: {}'.format(metros, cm))
print('{} metros em milimetros é: {}'.format(metros, mm))
