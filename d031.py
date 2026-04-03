from math import trunc
dist = float(input('Digite a distancia da viagem em Km: '))
distf = trunc(dist)
if distf <= 200:
    valor1 = 0.5 * distf
    print('O valor da viagem vai ser de R${:.2f}'.format(valor1))
else:
    valor2 = 0.45 * distf
    print('O valor da viagem vai ser de R${:.2f}'.format(valor2))
