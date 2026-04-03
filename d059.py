opcao = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while opcao != 5:
    maior = 0
    if n1 > maior:
        maior = n1
        if n2 > maior:
            maior = n2
    print('''Voce deseja:
    [1] somar
    [2] multiplicar
    [3] saber o maior
    [4] digitar novos numeros
    [5] sair do programa''')
    opcao = int(input('Sua opcao: '))
    if opcao == 1:
        print('A soma de {} mais {} eh igual a {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicacao de {} * {} eh igual a {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        print('O maior numero entre {} e {} eh {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Voltando a area de selecionar valores')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao != 5:
        print('Opcao Invalida')
print('Fim do programa')
