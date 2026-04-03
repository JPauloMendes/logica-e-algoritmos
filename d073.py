tabela = ('Atlético-MG', 'Botafogo', 'Athletico-PR', 'Chapecoense', 'Coritiba', 'Flamengo', 'Vasco da Gama', 'Cruzeiro', 'Bahia', 'EC Vitória', 'Fluminense', 'Grêmio', 'Mirassol', 'Bragantino' ,'Remo' ,'Santos' ,'São Paulo' , 'Corinthians', 'Internacional', 'Palmeiras')
print('-'*30)
print(f'A lista de times do Brasileirao: {tabela}')
print('-'*30)
print(f'Os 5 primeiros colocados sao {tabela[:5]}')
print('-'*30)
print(f'Os 4 ultimos colocados sao {tabela[16:]}')
print('-'*30)
print(f'Em ordem alfabetica fica {sorted(tabela)}')
print('-'*30)
for cont in range(0, len(tabela)):
    if tabela[cont] == 'Chapecoense':
        print(f'O time Chapecoense esta na {cont + 1} posicao')