resposta = 'S'
nome = nbarato = ''
total = cont = mbarato = 0
while resposta == 'S':
    nome = str(input('Digite o nome do produto: '))
    preco = int(input('Digite o preço do produto: '))
    total += preco
    if preco > 1000:
        cont += 1
    if cont == 1:
        mbarato = preco
        nbarato = nome
    if preco < mbarato:
        nbarato = nome
    while True:
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
print(f'''O total da compra foi R${total}
{cont} dos produtos custam mais de R$1000.00
O produto mais barato foi {nbarato} que custa R${mbarato}''')