resposta = 'S' 
maiorde18 = homem = mulher = 0
sexo = ''
while resposta == 'S':
    idade = int(input('Digite sua idade: '))
    if idade > 18:
        maiorde18 += 1
    while True:
        sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
        if sexo in 'FM':
            break
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    while True:
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
print(f'{maiorde18} pessoas sao maiores de 18 anos. Sabe-se que {homem} sao homens e {mulher} mulheres tem menos de 20 anos')
