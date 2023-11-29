'''Faça um programa que leia a medida de 3 retas e diga se essas retas podem formar um triangulo. '''

#lendo o comprimento das 3 retas
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
#aplicando a regra matemática para verificar se pode ser um triangulo.
if a < b + c and b < a + c and c < a + b: #para formar um triagulo um dos segmentos tem que ser menor que a soma dos outros dois. 
    print('Os Segmentos acima PODEM formar um triangulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triangulo!')
