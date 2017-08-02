# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço com 5% de desconto

preco = float(input('Digite o valor do produto: '))
desc = preco*0.15

print('O preço com 15% de desconto é: {}'.format(preco-desc))
