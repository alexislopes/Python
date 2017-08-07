# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.

# Para salários superiores a R$ 1.250,00 calcule um aummento de 10%
# Para ps  inferiores ou iguais, o aumento é de 15%

sal = float(input('Digite o salário: '))
if sal > 1250.00:
    nsal = sal*.10 + sal
    print('Novo salário: {}'.format(nsal))
    print('Salário antigo: {}'.format(sal))
else:
    nsal = sal*.15 + sal
    print('Novo salário: {}'.format(nsal))
    print('Salário antigo: {}'.format(sal))
