l = int(input('Digite a largura da parede: '))
h = int(input('Digite a altura da parede: '))
a = l * h
t = a / 2
print('A area dessa parede é {}m^2 e será necessário {:.2f} litros de tinta para pintar a parede'.format(a, t))