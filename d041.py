import datetime
idade = int(input('Digite o ano de nascimento: '))
ano = datetime.date.today().year
if ano - idade <= 9:
    print('MIRIM')
elif ano - idade <= 14:
    print('INFATIL')
elif ano - idade <= 19:
    print('JUNIOR')
elif ano - idade <= 20:
    print('SENIOR')
else:
    print('MASTER')