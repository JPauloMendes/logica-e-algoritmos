a1 = int(input('Digite o primeiro termo da sequencia: '))
razao = int(input('Digite a razao da sequencia: '))
a = 1
while a != 11:
    an = a1 + (a - 1) * razao
    a += 1
    print('{} → '.format(an), end='')
print('FIM')
