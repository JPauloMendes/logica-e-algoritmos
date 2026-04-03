salario = float(input('Qual seu salario: '))
if salario > 1250.00:
    print('Seu salario com o aumento eh de {}{:.2f}{}'.format('\033[4;32m', salario + (10 / 100 * salario), '\033[m'))
else:
    print('Seu salario com o aumento eh de {}{:.2f}{}'.format('\033[7m', salario + (15 / 100 * salario), '\033[m'))