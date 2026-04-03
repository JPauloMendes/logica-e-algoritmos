cont50 = cont20 = cont10 = cont1 = 0
valor = int(input('Digite o valor a ser sacado: '))
while True:
    while valor >= 50:
        valor -= 50
        cont50 += 1
    while valor >= 20:
        valor -= 20
        cont20 += 1
    while valor >= 10:
        valor -= 10
        cont10 += 1
    while valor >= 1:
        valor -= 1
        cont1 += 1
    break
if cont50 >= 1:
    print(f'{cont50} cedulas de R$50')
if cont20 >= 1:
    print(f'{cont20} cedulas de R$20')
if cont10 >= 1:
    print(f'{cont10} cedulas de R$10')
if cont1 >= 1:    
    print(f'{cont1} cedulas de R$1')