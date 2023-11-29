produto = float(input('Qual o valor do produto: R$ '))
desc = float(produto - (produto * 5 / 100))
print('O produto com valor de R${:.2f} com desconto de 5% vai custar R${:.2f}'.format(produto, desc))
