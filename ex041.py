'''Crie um programa que leia o ano de nascimento de um atleta e diga a sua categoria de acordo com a sua idade
– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

from datetime import date
#Pergunta data nascimento atleta
nascimento = int(input('Digite seu ano de nascimento:'))

#pega o ano atual do sistema através do módulo date e joga em uma váriavel
ano = date.today().year

#calcula idade atleta
idade = ano - nascimento
print('O atleta tem {} anos'.format(idade))

#bloco de condicionamento, verificação da classificação dos atletas.
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Calssificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')
