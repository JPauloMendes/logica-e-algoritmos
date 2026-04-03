lista = []
for a in range(1, 6):
    lista.append(int(input(f'Digite o {a}° valor: ')))
print(f'o menor valor foi {min(lista)}, ele esta na posicao {lista.index(min(lista)) + 1}')
print(f'o maior valor foi {max(lista)}, ele esta na posicao {lista.index(max(lista)) + 1}') 
