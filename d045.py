import random
jogador = str(input('Escolha entre pedra, papel e tesoura: '))
possibilidades = ['pedra', 'papel', 'tesoura']
pc = random.choice(possibilidades)
if pc == 'pedra' and jogador == 'papel' or pc == 'papel' and jogador == 'tesoura' or pc == 'tesoura' and jogador == 'pedra':
    print('Voce venceu! o pc escolheu {} e vc {}'.format(pc, jogador))
elif pc == 'papel' and jogador == 'pedra' or pc == 'tesoura' and jogador == 'papel' or pc == 'pedra' and jogador == 'tesoura':
    print('\033[;31;mVoce perdeu! o pc escolheu {} e vc {}\033[;31;m'.format(pc, jogador))
else:
    print('Empate! o pc escolheu {} e vc {}'.format(pc, jogador))