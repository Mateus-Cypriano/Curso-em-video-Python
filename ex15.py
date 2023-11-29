dias = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos Km foram rodados? '))
aluguel = float((dias * 60) + (km * 0.15))
print('O valor do aluguel será de: R${:.2f}'.format(aluguel))
