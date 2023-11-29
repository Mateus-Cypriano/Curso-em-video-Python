salário = float(input('Qual o salário do funcionário? R$'))
aumento = salário + (salário * 15 / 100)
print('O salário R${:.2f} do funcionário com 15% de aumento passa a ser R${:.2f}'.format(salário, aumento))
