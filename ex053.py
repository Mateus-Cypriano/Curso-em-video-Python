'''Faça um programa que leia uma frase e informe se ela é um palindromo.'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto)-1, -1, -1):
    inverso += junto[c]
print('O inverso da frase {} é {}.'.format(junto, inverso))
if junto == inverso:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo.')
    