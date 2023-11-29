'''Crie um programa que leia o nome completo do usuário e mostre o primeiro e o ultimo nome. '''

nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()
print('O seu primeiro nome é: {}.'.format(separado[0]))
print('O seu ultimo nome é: {}.'.format(separado[len(separado) - 1]))
