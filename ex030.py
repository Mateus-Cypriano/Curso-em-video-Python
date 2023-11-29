#criar um programa que identifique se um número é PAR ou ÍMPAR
num = int(input('Digite um número: ')) #input para escolha do número
resultado = num % 2 #resto da divisão do número por 2.
if resultado == 0:    #pelo principio matemático todo número par ter seu resto de divisão por 2 igual a 0
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))
