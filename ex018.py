import math#importar modulo math.
ang = float(input('Digite um angulo:'))
sen = math.sin(math.radians(ang))#utilizar modulo sin para calcular o seno. e utilizar o modulo radians para transformar em radiandos.
print('O angulo de {} tem o SENO igual a {:.2f}.'.format(ang,sen))
cos = math.cos(math.radians(ang))#utilizar o modulo cos para calcular cosseno e utilizar modulo radians para transformar em radiandos.
print('O angulo {} tem o COSSENO igual a {:.2f}.'.format(ang,cos))
tan = math.tan(math.radians(ang))#utilizar o modulo tan para calcular a tangente e utilizar o modulo radians para transformar em radiandos.
print('O angulo {} tem a TANGENTE igual a {:.2f}.'.format(ang,tan))

'''O método sin, cos e tan não aceita os valores dos angulos em graus Cº, somente em radiandos, por isso, convertemos o valor com o math.radians
assim, transformando o valor do grau em radiando e nos dando a resposta correta dentro do método sin,cos e tan.'''
