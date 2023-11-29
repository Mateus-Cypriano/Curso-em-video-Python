'''Crie um programa que mostre na tela todos os números pares que estão em um intervalo entre 1 e 50.'''
from time import sleep
#Dentro do laço o ultimo número do intervalo é sempre desconsiderado, colocar um número acima.
for c in range(1, 51):
    if c % 2 == 0: #condição do laço, se o resto da divisão por 2 for igual a 0, significa que ele é PAR.
        sleep(0.3)
        print(c, end = ' ')  #escreve na tela, somente os números do laço de repetição que atendem os requisitos da condição.

print('Esses são todos os números pares dentro do intervalo entre 1 e 50.')
print('FIM')
