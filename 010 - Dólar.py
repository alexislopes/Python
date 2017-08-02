# Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode comprar

# considere uss1,00 = RS3,27


cash = float(input('Quantos reais você tem? '))
print('Então você consegue comprar {:.2f} dólares'.format(cash/3.27))
