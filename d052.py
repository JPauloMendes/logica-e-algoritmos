n = int(input('Digite um numero inteiro: '))
cont = 0
for a in range(1, n+1):
    if n % a == 0:
        cont += 1
if cont == 2:
    print('O numero digitado eh primo!')
else:
    print('O numero digitado NAO eh primo')