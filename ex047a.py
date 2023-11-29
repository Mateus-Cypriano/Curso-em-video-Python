'''Crie um programa que mostre na tela todos os números pares que estão em um intervalo entre 1 e 50.'''
from time import sleep
#Dentro do laço o ultimo número do intervalo é sempre desconsiderado, colocar um número acima.
for c in range(2, 51, 2):
        print(c, end = ' ')  #não utiliza uma condição a lógica está dentro do laço. Começa do número 2 pois o n1 pode ser descartado e pula de 2 em 2, assim só pegando os pares e economizando memória.

print(' ')
print('Esses são todos os números pares dentro do intervalo entre 1 e 50.')
print('FIM')
