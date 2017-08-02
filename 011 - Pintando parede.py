# Faça um programa que leia a largura e a altura de uma parede em metros
# calcule a sua área e a quantidade de tinta necessária para pinta-la
# sabendo que cada litro de tinta pinta uma area de 2m²

largura = float(input('Largura da parede(m): '))
altura = float(input('Altura da parede(m): '))


area = altura * largura

print('Dimensão da parede {}x{} cujo a área é: {}m²'.format(largura, altura, area))
print('você precisará de {}L de tinta'.format(area/2))
