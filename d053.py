frase = str(input('Digite uma frase para checar se ela eh um palindromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('A frase eh um palindromo! {} se torna {}'.format(junto, inverso))
else:
    print('A frase NAO eh um palindromo! {} se torna {}'.format(junto, inverso))