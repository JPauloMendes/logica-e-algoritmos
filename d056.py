tot = 0
maisvelho = 0
qntsm = 0
nomemaisvelho = ''
for a in range(1, 5):
    nome = str(input('Digite o nome da {}° pessoa: '.format(a))).title()
    idade = int(input('Digite a idade da {}° pessoa: '.format(a)))
    print('''Digite o sexo da {}° pessoa
M para Masculino e F para Feminino'''.format(a))
    sexo = str(input('Sua opcao: ')).strip().upper()
    tot += idade
    if sexo == 'M':
        if idade > maisvelho:
            maisvelho = idade
            nomemaisvelho = nome
    elif sexo == 'F':
        if idade < 20:
            qntsm += 1
    else:
        print('Input Invalido!')
media = tot/a
print('A media da idade do grupo eh igual a {}'.format(media))
print('O homem mais velho eh {} com {} anos'.format(nomemaisvelho, maisvelho))
print('A quantidade de mulheres com menos de 20 anos eh {}'.format(qntsm))
