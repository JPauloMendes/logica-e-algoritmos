nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1 + nota2) / 2
if m > 7:
    print('Parabens vc passou com a media de {}'.format(m))
elif m < 5:
    print('\033[1;31;43mRapaz, nao sobrou nada pra voce(beta), ficou com a media de {}\033[m'.format(m))
else:
    print('Vc esta de recuperacao kkkk')