'''Faça um programa que calcule a soma entre todos os números IMPARES que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
soma = 0
cont = 0
for c in range(3, 501, 3):
    if c % 2 == 1:
        cont = cont + 1
        soma = soma + c
print('O somatório de todos os {} números solicitados é igual a: {}'.format(cont, soma))