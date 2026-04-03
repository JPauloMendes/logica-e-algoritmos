n1 = int(input('Digite um numero inteiro: '))
print('''Que tipo de operacao voce deseja:
[1] para soma
[2] para subtracao
[3] para multiplicacao
[4] para divisao''')
tipo = int(input('sua opcao: '))
if tipo == 1:
    for a in range(0, 11):
        print('{} + {} = {}'.format(n1, a, n1 + a))
if tipo == 2:
    for a in range(0, 11):
        print('{} - {} = {}'.format(n1, a, n1 - a))
if tipo == 3:
    for a in range(0, 11):
        print('{} x {} = {}'.format(n1, a, n1 * a))
if tipo == 4:
    for a in range(0, 11):
        if a == 0:
            print('Impossivel calcular')
        else:
            print('{} / {} = {:.2f}'.format(n1, a, n1 / a))
