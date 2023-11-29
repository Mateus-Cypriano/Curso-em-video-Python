'''Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date

atual = date.today().year
maior_idade = 0
menor_idade = 0
for c in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa:'.format(c)))
    if atual - nascimento >= 21:
        maior_idade += 1
    else:
        menor_idade +=1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior_idade))
print('Também tivemos {} pessoas menores de idade.'.format(menor_idade))
