valor = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), 
int(input('Digite mais um valor: ')), int(input('Digite o ultimo valor: ')))
print(f'Voce digitou os valores {valor}')
print(f'Apareceram {valor.count(9)} numeros 9')
if 3 in valor:
    print(f'O valor 3 apareceu na {valor.index(3) + 1}° posicao')
else:
    print(f'Nao foi digitado nenhum valor 3')
print('Os valores pares digitados foram: ', end='')
for n in valor:
    if n % 2 == 0:
        print(n, end=' ')