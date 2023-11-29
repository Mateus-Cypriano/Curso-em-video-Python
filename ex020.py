from random import shuffle
'''Faça um programa que leia o nome de quatro alunos e apresente a ordem de apresentação de um trabalho aleatóriamente.'''
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação dos trabalhos será: {}'.format(lista))
