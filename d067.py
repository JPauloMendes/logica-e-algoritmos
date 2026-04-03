a = 1
cont = 0
while True:
    print('-'*30)
    n = int(input('Deseja ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*30)
    while a != 11:
        print(f'{n} x {a} = {n*a}')
        a += 1
    a = 1
    cont += 1
print(f'FIM DO PROGRAMA. VOCE VIU {cont} TABUADAS')