'''Desenvolva um programa que leia a altura e o peso de uma pessoa e calcule seu IMC
e mostre na tela seu status de acordo com a tabela a seguir:
– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

#lendo dados do usuário, peso e altura.
peso = float(input('Digite seu peso: (kg)'))
altura = float(input('Digite sua altura: (m)'))
#calcula o IMC do usuário. Kg/m²
imc = peso / altura**2
print('Seu IMC é {:.2f}'.format(imc), end = ' ')
if imc < 18.5:
    print('Cuidado você está ABAIXO do peso')
elif imc <= 24.99:
    print('Parabéns você está no peso ideal!')
elif imc <= 29.99:
    print('Cuidado, você está com SOBREPESO.')
elif imc <= 39.99:
    print('Cuidado, você está com OBESIDADE.')
elif imc >= 40:
    print('ATENÇÃO, você está com OBESIDADE MÓRBIDA, tome cuidado.')
