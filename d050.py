soma = 0
contador = 0
for a in range(1, 7):
    num = int(input('Digite o {}° numero: '.format(a)))
    if num % 2 == 0:
        soma += num
        contador += 1
print('Vc digitou {} numeros pares e a soma deles eh igual a {}'.format(contador, soma))