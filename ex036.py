'''Crie um programa para aprovar um emprestimo para uma compra de uma casa
Pergunte o valor da casa, o salário da pessoa que vai comprar e em quantos anos ele pretende pagar.
A prestação da casa não pode exceder 30% do salário ou o empréstimo será negado. '''

#lendo as variaveis principais, valor da casa, salário e em quanto tempo será pago.
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do salário? R$'))
tempo = int(input('Quantos anos de financiamento?'))
prestacao = float(casa / tempo / 12) #calculando o valor da prestação necessária de acordo com o financiamento da casa.
#criando o bloco de condicionamento.
if prestacao > salario * 30 / 100:
    print('Uma casa no valor de R${:.2f}, com financiamento em {} anos, vai ter uma prestação de R${:.2f} por mês.'.format(casa, tempo, prestacao))
    print('Empréstimo \033[1;31m NEGADO \033[m')
elif prestacao >= salario * 20 / 100 and prestacao <= salario * 30 / 100:
    print('Uma casa no valor de R${:.2f}, com o financiamento em {} anos, vai ter uma prestação de R${:.2f} por mês.'.format(casa, tempo, prestacao))
    print('O valor da prestação está um pouco, alto, porém o empréstimo pode ser \033[1;33m CONCEDIDO\033[m')
else:
    print('Uma casa no valor de R${:.2f}, com financiamento em {} anos, vai ter uma prestação de R${:.2f} por mês.'.format(casa, tempo, prestacao))
    print('Muito bem, empréstimo \033[1;32mCONCEDIDO\033[m!!')
