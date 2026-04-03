import datetime
idade = int(input('Digite seu ano de nascimento: '))
ano = datetime.date.today().year
if ano - idade > 18:
    print('Ja se passaram {} anos do prazo de alistamento'.format(ano - idade - 18))
elif ano - idade == 18:
    print('Deve alistar-se esse ano!')
else:
    print('Deve alistar-se daqui a {} anos'.format(idade - ano + 18))