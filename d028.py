from random import randint
n = randint(0, 5)
chute = int(input('Chute um numero inteiro entre 0 e 5: '))
if chute == n:
    print('Parabens voce acertou!')
else:
    print('Infelizmente voce errou! Eu pensei no numero {} e nao no numero {}'.format(n, chute))