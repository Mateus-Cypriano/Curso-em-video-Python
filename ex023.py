num = int(input('Digite um número entre 0 e 9999:  '))
u=num // 1 % 10
d=num // 10 % 10
c=num // 100 % 10
m=num // 1000 % 10
min = int(0);
max = int(9999)
if num > max:
    print('O número digitado é maior que 9999. Impossível calcular!')

elif num < min:
    print('O número digitado é menor que 0. Impossível calcular!')

else:
    print('A unidade desse número é: {}'.format(u))
    print('A dezena desse número é: {}'.format(d))
    print('A centena desse número é: {}'.format(c))
    print('O milhar desse número é: {}'.format(m))
