''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
media = 0
nomevelho = ''
idadevelho = 0
totmulher20 = 0
for p in range(1, 5):
    print('------- {}ªPessoa -------'.format(p))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Sexo: [M/F]:')).strip().upper()
    media += idade
    if p == 1 and sexo in 'Mm':
        nomevelho = nome
        idadevelho = idade
    if sexo in 'Mm' and idade > idadevelho:
        nomevelho = nome
        idadevelho = idade
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

print('A média de idade do grupo é de {.:1f} anos.'.format(media / p))
print('O homem mais velho se chama {} e tem {} anos'.format(nomevelho, idadevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
