frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase.'.format(frase.lower().count('a')))
print('A primeira vez que a letra A apareceu na frase foi na posição {}.'.format(frase.lower().find('a') + 1 ))
print('A ultima vez que a letra A apareceu na frase foi na posição {}.'.format(frase.lower().rfind('a') + 1)) #utilizando o rfind para procurar a primeira ocorrencia a partir da direita
