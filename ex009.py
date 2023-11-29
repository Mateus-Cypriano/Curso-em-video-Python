real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = float(real/4.90)
print('com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))
