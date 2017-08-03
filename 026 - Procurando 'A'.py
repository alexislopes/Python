# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra 'A'
# Em que posição ela aparece a primeira vez.
# em que posição ela aparece a ultima vez.

frase = input('Digite uma frase: ').lower()

print('Aparece(m) {} vez(es) a letra "A" '.format(frase.count('a')))
if frase.count('a') > 0:
    print('Aparece primeiro na posição {}'.format(frase.find('a')))
    print('Aparece pela última vez na posição {}'.format(frase.rfind('a')))
