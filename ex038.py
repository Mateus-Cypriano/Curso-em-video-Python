'''Crie um programa que leia dois números inteiros e os compare
mostrando na tela a mensgagem:
O primeiro número é maior
O segundo número é maior
Não existe número maior, ambos os números são iguais.'''

from time import sleep
a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
print('\033[1;34mPROCESSANDO...\033[m')
sleep(2)
if a > b:
    print('O \033[1;36mPRIMEIRO\033[m número digitado ({}) é maior que o \033[1;36mSEGUNDO\033[m número digitado ({})'.format(a, b))
elif a < b:
    print('O \033[1;36mSEGUNDO\033[m número digitado ({}) é maior que o \033[1;36mPRIMEIRO\033[m número digitado ({})'.format(b, a))
else:
    print('\033[1;36mNENHUM\033[m dos números é maior que o outro. Ambos são \033[4;32mIGUAIS\033[m.')
