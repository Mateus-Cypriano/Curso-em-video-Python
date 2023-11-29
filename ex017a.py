import math
ca = float(input('comprimento do cateto adjacente:'))
co = float(input('comprimento do cateto oposto:'))
hi = math.hypot(ca, co)
print('A hipotenusa vai medir: {:.2f}'.format(hi))
'''utilizando o modulo math para calcular a hipotenusa através do método hypot, sem precisar 
utilizar o conceito matemático.'''
