nome = str(input('Digite seu nome: ')).strip()
nomec = nome.split()
print('O primeiro nome eh: {}'.format(nomec[0],))
print('Seu ultimo nome eh: {}'.format(nomec[len(nomec)-1]))