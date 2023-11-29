cidade = str(input('Digite o nome da sua cidade: ')).strip()
print('SANTO' in cidade.upper())

'''outra maneira de se fazer esse código rodar seria utilizando os indicies da palavra Santo. 
Por exemplo: como a palavra tem 5 letras utilizariamos do fatiamento [:5] para contar a palavra inteira e depois passar tudo para maisculo, minusculo
como na maneira acima.'''

#por exemplo:
print(cidade[:5].upper() == 'SANTO')#joguei tudo para maíscula
print(cidade[:5].lower() == 'santo')#joguei tudo para minúscula
print(cidade[:5].capitalize() == 'Santo')#Captalizei a palavra.
