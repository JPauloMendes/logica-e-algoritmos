preco = float(input('Digite o preco do produto: '))
pagamento = str(input('Qual o tipo de pagamento(dinheiro, cheque ou cartao)? '))
vezes = int(input('Digite quantas vezes quer parcerlar a compra(apenas cartao e ate 12x): '))
pagamento = pagamento.lower()
if pagamento == 'dinheiro' or pagamento == 'cheque':
    print('O preco sera R${:.2f}'.format(preco - (10/100 * preco)))
elif pagamento == 'cartao' and vezes == 1 or vezes == 0:
    print('O preco sera R${:.2f}'.format(preco - (5/100 * preco)))
elif vezes == 2:
    print('O preco sera R${:.2f} e a parcela de R${} em 2 vezes'.format(preco, preco/2))
elif vezes <= 12:
    print('O preco sera R${:.2f} e a parcela de R${:.2f} em {} vezes'.format(preco + (20/100 * preco), (preco + (20/100 * preco)) / vezes, vezes))
else:
    print('Tipo de pagamento invalido!')