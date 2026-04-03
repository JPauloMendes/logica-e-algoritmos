velocidade = float(input('Digite a velocidade do carro em Km/h: '))
multa = 7 * (velocidade - 80)
if velocidade > 80:
    print('Voce foi multado pois ultrapassou o limite, a multa eh de R${:.2f}'.format(multa))
else:
    print('Voce nao foi multado')