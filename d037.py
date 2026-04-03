n = int(input('Digite um numero inteiro: '))
print('''Qual base voce deseja converter?
[ 1 ] para converter para BINARIO
[ 2 ] para converter para OCTAL
[ 3 ] para converter para HEXADECIMAL''')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print('{} convertido para BINARIO eh {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL eh {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL eh {}'.format(n, hex(n)[2:]))
else:
    print('Opçao Invalida')