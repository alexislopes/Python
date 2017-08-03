# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome 'SANTO'

cidade = input('Digite o nome de uma cidade: ').lower().split()
if cidade[0] == 'santo':
    print('Começa')
else:
    print('Não começa')
