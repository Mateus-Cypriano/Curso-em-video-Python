'''Faça um programa que leia o sexo de uma pessoa mas só aceite os valores 'M' ou 'F'
caso esteja errado peça a digitação novamente até ser digitado corretamente.'''

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe seu sexo: [M/F]')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Caractere inválido, por favor, digite novamente!')
    else:
        print('Sexo {} registrado com sucesso'.format(sexo))
print('Fim')
