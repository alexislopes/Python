# Faça um programa que leia um número
# inteiro qualquer e mostre na tela sua tabuada.

num = int(input('Digite um número: '))
cont = 0
while cont <= 10:
    print('{} x {} = {}'.format(cont, num, cont*num))
    cont+=1
