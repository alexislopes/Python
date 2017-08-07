# Desenvolva um programa que pergunte a distancia de umma viagem em KM
# Calcule o preço da passagem, cobrando R$0,50 por KM para viagens até 200KM
# e R$0.45 para viagens mais longas.

dis = float(input('Qual a distancia da viagem(KM)? '))
if dis <= 200.0:
    print('Você deverá pagar {}'.format(dis*0.50))
else:
    print('Você deverá pagar {}'.format(dis*0.45))
