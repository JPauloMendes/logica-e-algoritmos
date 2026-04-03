extenso = ('ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONDE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
resposta = 'S'
while resposta == 'S':    
    while True:
        n = int(input('Digite um valor inteiro entre 0 e 20: '))
        if n >= 0 and n <= 20:
            break
    for cont in range(0, len(extenso)):
        if cont == n:
            print(f'O numero digitado foi {extenso[cont]}')
    resposta = str(input('Deseja ver outro numero? [S/N]')).strip().upper()[0]
print('Fim do Programa')