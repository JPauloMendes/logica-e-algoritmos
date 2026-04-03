d = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos Km o carro percorreu? '))
preco = float((d * 60) + (km * 0.15))
print('O preco a pagar pelo aluguel do carro eh de R${}'.format(preco))