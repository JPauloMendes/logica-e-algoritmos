listagem = ('Papel', 0.50, 'Borracha', 1, 'Caneta', 1.50, 'Caderno', 20)
nome = 'LISTAGEM DE PRECO'
print('-'*50)
print(nome.center(50))
print('-'*50)
for a in range(0, len(listagem)):
    if a % 2 == 0:
        print(f'{listagem[a]:.<30}', end='')
    else:
        print(f'R${listagem[a]:>.2f}')