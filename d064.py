n = 0
cont = 0
soma = 0
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um numero inteiro (Digite 999 para parar): '))
print('Foram digitados {} numeros e a soma deles eh igual a {}'.format(cont, soma))
