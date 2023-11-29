'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''
#print estetico
print('{:=^40}'.format((' LOJAS TABAJARA ')))
#recebe o valor total das compras
compras = float(input('Qual o valor das suas compras? R$'))
#exibe na tela as formas de pagamento
print('''FORMAS DE PAGAMENTO:
[1] Á vista dinheirou / cheque.
[2] Á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão 
''')
#recebe a informação do usuário de qual será a forma de pagamento de acordo com a lista acima.
opção = int(input('Qual a forma de pagamento?'))
#bloco de verificação das condições.
if opção == 1:
    total = compras - (compras * 10 / 100)
    print('Comprando a vista no dinheiro ou cheque, você terá um desconto de 10%.')
elif opção == 2:
    total = compras - (compras * 5 / 100)
    print('Comprando a vista no cartão, você terá um desconto de 5%.')
elif opção == 3:
    total = compras
    parcela = total / 2
    print('A sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    totparcelas = int(input('Quantas vezes você deseja parcelar?'))
    total = compras + (compras * 20 / 100)
    parcela = total / totparcelas
    print('Suas compras seram parceladas em {}x COM JUROS de 20%. O valor das suas parcelas será de R${:.2f}'.format(totparcelas, parcela))
else:
    total = compras
    print('\033[1;31mOPÇÃO INVALIDA DE PAGAMENTO. Por favor, tente novamente!\033[m')
print('O valor total das suas compras foi de R${:.2f}. O valor final será de R${:.2f}.'.format(compras, total))
