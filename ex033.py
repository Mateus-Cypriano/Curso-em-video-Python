n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
#verificando o menor
menor = n1  #posso considerar um dos valores como menor e só validar os outros dois, assim eliminando uma linha de if no código.
if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3
#verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3
print('O menor número é: {}'.format(menor))
print('O maior número é: {}'.format(maior))
