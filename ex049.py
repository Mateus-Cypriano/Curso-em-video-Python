'''Recrie uma tabuada de um número utilizando laços de repetição.'''
n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} X {:2} = {:2}'.format(n, c, n * c))
print('FIM')
