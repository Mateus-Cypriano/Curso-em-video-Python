'''Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artificios
indo de 10 até 0 com uma pausa de 1 segundo entre elas.'''
from time import sleep
import emoji

for c in range(10, -1, - 1):
    print(c)
    sleep(1)

print(emoji.emojize(':fireworks:'))
