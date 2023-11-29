d = int(input('Quantos dias o carro ficou alugado?'))
km = int(input('Quantos km foram rodados?    km'))
a = float((60 * d) + (0.15 * km))
print('O valor do aluguel do carro foi de R${}'.format(a))
