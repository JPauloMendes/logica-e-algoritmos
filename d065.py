resposta = ''
n = maior = menor = cont = soma = 0
while resposta != 'N':
    n = int(input('Digite um valor: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    if cont == 0:
        menor = n
    cont += 1
    soma += n
    media = soma/cont
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print('Voce digitou {} numeros e a media foi {}. O maior valor foi {} e o menor foi {}'.format(cont, media, maior, menor))