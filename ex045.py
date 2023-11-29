'''Crie um programa que jogue Jokenpô com você'''

from random import choice
from time import sleep
print('\033[1;31m{:=^40}\033[m'.format(' JO-KEN-PÔ '))
print('''Vamos jogar Jo-ken-Pô?  
[1] Sim
[2] Não
[3] Como se joga?''')  # MENU INTERATIVO DO JOGO.
opção = int(input('Digite uma opção: ')) #O usúario digita a opção desejada, se quer jogar, se não quer jogar ou se quer saber como se joga.
if opção == 1: #bloco verdadeiro. roda o jogo.
    # criando 3 variavéis que serão utilizadas para transformação da escolha do usuário de número inteiro para strings.
    pedra = str('Pedra').capitalize()
    papel = str('Papel').capitalize()
    tesoura = str('Tesoura').capitalize()

    #criando uma lista com 3 possíveis escolhas, pedra, papel ou tesoura. Todas em string.
    jogo = ['Pedra', 'Papel', 'Tesoura']
    #Fazendo o computador escolher aleatóriamente uma das três opções.
    computador = choice(jogo)
    #Menu interativo dentro do jogo. O usuário deve escolher dentro das 3 opções possíveis.
    print('''Escolha entre Pedra, Papel ou Tesoura:
    [ 1 ] Pedra
    [ 2 ] Papel
    [ 3 ] Tesoura''')

    #Jogador escolhe de acordo com o número da opção em formato de número inteiro.
    jogador = int(input('Digite sua escolha: '))

    #Bloco de verificação onde ocorre a transformação da escolha do usuário para String e compara com a 'escolha' do computador.
    if jogador == 1:
        jogador = pedra
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('PÔ!!!')
        sleep(1)
        print('O Computador escolheu {}.'.format(computador))
        print('O Jogador escolheu {}.'.format(jogador))
        if computador == 'Tesoura':
            print('Parabéns! Você me venceu! :(')
        elif computador == 'Papel':
            print('HAHAHA, eu Venci! :)')
        else:
            print('Parece que empatamos. Finalmente um oponente digno!')

    elif jogador == 2:
        jogador = papel
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('PÔ!!!')
        sleep(1)
        print('O Computador escolheu {}.'.format(computador))
        print('O Jogador escolheu {}.'.format(jogador))
        if computador == 'Pedra':
            print('Parabéns! Você me venceu!')
        elif computador == 'Tesoura':
            print('HAHAHA, eu venci! :)')
        else:
            print('Parece que empatamos. Finalmente um oponente digno!')

    elif jogador == 3:
        jogador = tesoura
        print('JO...')
        sleep(1)
        print('KEN...')
        sleep(1)
        print('PÔ!!!')
        sleep(1)
        print('O Computador escolheu {}.'.format(computador))
        print('O Jogador escolheu {}.'.format(jogador))
        if computador == 'Papel':
            print('Parabéns! Você me venceu! :(')
        elif computador == 'Pedra':
            print('HAHAHA, eu venci! :)')
        else:
            print('Parece que empatamos. Finalmente um oponente digno!')

    else:
        print('\033[1;31mOPÇÃO INVALIDA. Por favor, tente novamente!\033[m')

elif opção == 2:
    print('Tudo bem, quando quiser jogar, basta me chamar.')

elif opção == 3:
    print('''jokenpô é um jogo em que as pessoas jogam com as mãos, escolhendo entre pedra, papel e tesoura.
    E funciona assim: a tesoura corta o papel, mas quebra com a pedra; 
    o papel embrulha a pedra, mas é cortado pela tesoura 
    e a pedra quebra a tesoura e é embrulhada pelo papel.''')
