from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.', end = ' ')
    print('Deu Par' if total % 2 == 0 else 'Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu.')
            v += 1
        else:
            print('Você Perdeu.')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu.')
            v += 1
        else:
            print('Você Perdeu.')
            break

    print('Vamos jogar novamente...')
print(f'você ganhou {v} vezes até perder')