n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda  nota:'))
m = float((n1+n2)/2)# Para calcular a média é preciso usar a ordem de precedencia, fazendo com que a soma seja prioritária e depois calcule-se a média.
print('A média das duas notas equivalem a {}.'.format(m))
