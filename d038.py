a = int(input('Digite um numero inteiro: '))
b = int(input('Digite um numero inteiro: '))
if a > b:
    print('o valor {} eh maior que {}'.format(a, b))
elif b > a:
    print('o valor {} eh maior que {}'.format(b, a))
else:
    print('Os valores sao iguais')