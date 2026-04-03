casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salario: R$'))
anos = int(input('Digite a quantidade de anos para pagar: '))
valormensal = casa / (anos * 12)
if valormensal <= (salario * 30 / 100):
    print('O emprestimo foi aprovado!! O valor da prestacao mensal sera de R${:.2f}'.format(valormensal))
else:
    print('Infelizmente o emprestimo foi negado')