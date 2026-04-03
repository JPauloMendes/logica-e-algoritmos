from random import randint
jogador = ''
pc = randint(0, 11)
cont = 0
while jogador != pc:
    jogador = int(input('Chute um numero entre 0 e 10: '))
    cont += 1
    if jogador > pc:
        print('Menos... Tente novamente')
    if jogador < pc:
        print('Mais... Tente novamente')
print('O PC pensou em {}! Parabens vc acertou em {} tentativas'.format(pc, cont))