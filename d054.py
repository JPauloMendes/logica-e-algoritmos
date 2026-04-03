from datetime import date
cont = 0
for a in range (1, 8):
    anonasc = int(input('Digite seu ano de nascimento: '))
    if date.today().year - anonasc >= 18:
        cont += 1
print('{} pessoas ja atingiram a maioridade e {} pessoas ainda vao'.format(cont, 7 - cont))