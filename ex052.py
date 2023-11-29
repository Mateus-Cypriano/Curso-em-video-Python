'''Faça um programa que leia um número inteiro e diga se ele é um número primo'''

n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, n+1):
   if n % c == 0:
       tot += 1
       print('\033[32m', end = '')
   else:
       print('\033[31m', end = '')
   print('{} '.format(c), end = '')
print('\033[m\nO número {} foi divisivel {} vezes.'.format(n, tot))
if tot == 2:
    print('E por isso ele é PRIMO.')
else:
    print('E por isso ele NÃO É PRIMO.')
