'''importando o random choice para sortear um nome dentro de uma lista.
mesmo conceito utilizado no projeto cara ou coroa, porém a lista é criada a partir do input do teclado, dentro das 4 váriaveis'''
from random import choice
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
r = choice([a1, a2, a3, a4])
print('O aluno escolhido foi: {}'.format(r))
