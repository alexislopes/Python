# Escreva um programa que leia a velocidade de um carro

# Se ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado

# A multa vai custar R$ por cada KM acima do limite.

vel = float(input('Qual a velocidade? '))
if vel > 80.0:
    multa = vel - 80.0
    multa = multa*7.0
    print('Você foi multado!\nValor da multa R${}'.format(multa))
