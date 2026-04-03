n1 = float(input('Digite um numero: ')) 
n2 = float(input('Digite um numero: ')) 
n3 = float(input('Digite um numero: '))
if n1 > n2 > n3:
    print('{} eh o maior'.format(n1))
else:
    if n2 > n1 > n3:
        print('{} eh o maior'.format(n2))
    else:
        print('{} eh o maior'.format(n3))
if n1 < n2 < n3:
    print('{} eh o menor'.format(n1))
else:
    if n2 < n1 < n3:
        print('{} eh o menor'.format(n2))
    else:
        print('{} eh o menor'.format(n3))