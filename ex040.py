"""Crie um programa que leia duas notas de um aluno e mostre se ele foi APROVADO ou REPROVADO de acordo com
a média dele:
 média abaixo de 5.0 - REPROVADO
 média entre 5.0 e 6.9 - RECUPERAÇÃO
 média acima de 7.0 - APROVADO"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = float((n1 + n2) / 2)
aprovado = float(7.0)
reprovado = float(4.9)
recuperacao = float(5.0)
if media >= aprovado:
    print('Parabéns, como sua média foi {:.2f} Você foi APROVADO.'.format(media))
elif media <= reprovado:
    print('Infelizmente como sua média foi de {:.2f}, você foi REPROVADO.'.format(media))
elif media >= recuperacao:
    print('Como sua média foi de {:.2f}, você deverá fazer uma RECUPERAÇÃO, se esforce!'.format(media))
