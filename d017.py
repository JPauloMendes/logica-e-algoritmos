from math import sqrt
catetooposto = float(input('Digite o comprimento do cateto oposto: '))
catetoadjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = ((catetoadjacente * catetoadjacente) + (catetooposto * catetooposto))
print('o valor da hipotenusa eh {}'.format(sqrt(hipotenusa)))