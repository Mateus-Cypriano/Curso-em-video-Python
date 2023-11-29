'''pelo principio matemático, a soma dos quadrados dos catetos é igual ao quadrado da hipotenusa
sendo assim, obtendo a medida do Cateto adjacente e do cateto oposto, basta somar os valores elevados a 2
e achar a raiz da hipotenusa^2'''
ca = float(input('Qual o comprimento do cateto adjacente?'))
co = float(input('Qual o comprimento do cateto oposto?'))
hq = (ca**2 + co**2) ** (1/2)#somando os quadrados dos catetos e elevando a meio. Mesma coisa que tirar a raiz.
print(f'A hipotenusa vai medir: {hq:.2f}') #nova forma de formatção??!
