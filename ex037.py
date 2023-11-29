'''crie um programa que leia e converta um número inteiro para um número na base binária,
octal ou hexadecimal'''
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases númericas para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[4;31mOpção inválida, por favor, tente novamente.\033[m')
