#exercício programa que calcula a velocidade de um veículo e a cada km ultrapassado do limite máximo será aplicado uma multa de R$7,00.
carro = int(input('Qual a velocidade do carro?'))#input no tipo int para verificar a velocidade do veículo
multa = float((carro-80)*7)#variavel multa calcula a diferença entre a velocidade e o limite de velocidade multiplicando pelo valor da multa que é R$7,00.
if carro > 80: #condição do programa, se o carro ultrapassar a velocidade limite aplica uma linha de códigos.
    print('Você está ultrapassando a velocidade limite que é 80Km/h e será multado em: R${:.2f}'.format(multa))#bloco verdadeiro da condição.
print('Tenha uma boa viagem!')
