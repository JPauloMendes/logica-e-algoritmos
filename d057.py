s = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while s not in 'FM':
    s = str(input('Opcao Invalida. Informe seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(s))
