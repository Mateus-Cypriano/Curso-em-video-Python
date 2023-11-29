from random import randint

computador = randint(0,10)
print('Sou seu Computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue acertar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente novamente.')
        else:
            print('Menos... tente novamente.')
print('Esse mesmo! Você acertou em {} tentativas.'.format(palpite))
