a = int(input('Digite o comprimento do primeiro lado: '))
b = int(input('Digite o comprimento do segundo lado: '))
c = int(input('Digite o comprimento do terceiro lado: '))
if a+b > c and a+c > b and b+c > a:
    print('\033[1;31;42m Eh possivel fazer um triangulo com esses segmentos\033[m')
else:
    print('\033[1;33;44m Nao eh possivel fazer um triangulo com esses segmentos\033[m')