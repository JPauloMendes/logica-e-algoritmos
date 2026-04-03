from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do angulo:'))
print('O angulo {} tem os valores no seno de {:.2f}, no cosseno de {:.2f}, na tangente de {:.2f} '.format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
