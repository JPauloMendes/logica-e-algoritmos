from random import randint
cont = 0
while True:
    pc = randint(1, 10)
    jogador = int(input('Diga um valor: '))
    while True:
        escolha = str(input('Par ou Impar? [P/I] ')).strip().upper()
        if escolha in 'PI':
            break
    soma = jogador + pc
    resultado = soma % 2
    if resultado == 0:
        nome = 'par'
    else:
        nome = 'impar'
    if escolha == 'P':
        print(f'Voce jogou {jogador} e o computador {pc}. O total deu {soma} e deu {nome}')
        if resultado == 0:
            print('Voce venceu! Jogue mais uma vez!')
        else:
            print('Voce perdeu!')
            break
    elif escolha == 'I':
        print(f'Voce jogou {jogador} e o computador {pc}. O total deu {soma} e deu {nome}')
        if resultado != 0:
            print('Voce venceu! Jogue mais uma vez!')
        else:
            print('Voce perdeu!')
            break
    cont += 1
print(f'Game Over! Voce venceu {cont} vezes')
      