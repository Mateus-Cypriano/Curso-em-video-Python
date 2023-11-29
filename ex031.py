from time import sleep #importação metodo sleep do módulo time
viagem = float(input('Qual a distancia em KM para o destino? ')) #input inicial, verificação distância percorrida na viagem
print('Calculando valor da passagem...') #linha código visual
sleep(1.5) #colocando o programa para 'dormir' por 2 segundos, além de visual em aplicações maiores pode ser um recurso útil para utilização da memória.
if viagem <= 200:  #condição do programa desejado
    valor = float(0.50) #bloco verdadeiro. Utilizando a variavel de valor dentro do bloco de condicionamento, para ser mais prático.
    print ('O valor da sua passagem será de: R${:.2f}. Cobrando R${:.2f} por Km rodado.'.format(valor*viagem, valor))
else:
    valor = float(0.45)
    print ('O valor da sua passagem será de: R${:.2f}. Cobrando R${:.2f} por km rodado.'.format(valor*viagem, valor))

