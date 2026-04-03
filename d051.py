a1 = int(input('Digite o primeiro termo da sequencia: '))
razao = int(input('Digite a razao da sequencia: '))
for a in range (1, 11):
    an = a1 + (a - 1) * razao
    print('A progressao eh:' \
    ' {} '.format(an))
