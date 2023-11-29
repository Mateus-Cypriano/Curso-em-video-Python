from random import randint
v = 0
while True:
    print('-'*40)
    print('PAR OU ÍMPAR')
    print('-'*40)
    escolha = input('Par ou Ímpar [P/I]'.upper().strip())
    jogador = int(input('Digite um número entre 1 a 10: '))
    comp = randint(1, 10)
    res = jogador + comp
    if escolha == 'p' and res % 2 == 0:
        print(f'Você jogou {jogador}, o computador jogou {comp}, deu um total de {res}. Deu PAR')
        print('PARABÉNS, VOCÊ GANHOU. VAMOS JOGAR NOVAMENTE.')
        v += 1
    elif escolha == 'p' and res % 2 == 1:
        print(f'Você jogou {jogador}, o computador jogou {comp}, deu um total de {res}. Deu IMPAR')
        print('VOCÊ PERDEU')
        break
    elif escolha == 'i' and res % 2 == 1:
        print(f'Você jogou {jogador}, o computador jogou {comp}, deu um total de {res}. Deu IMPAR')
        print('PARABÉNS, VOCÊ GANHOU. VAMOS JOGAR NOVAMENTE.')
        v += 1
    elif escolha == 'i' and res % 2 == 0:
        print(f'Você jogou {jogador}, o computador jogou {comp}, deu um total de {res}. Deu PAR')
        print('VOCÊ PERDEU')
        break

print(f'Você ganhou {v} vez(es) consectivas até perder.')

