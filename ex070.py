totalG = maismil = menor = cont =  0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('valor do produto: R$'))
    resp = ' '
    totalG += valor
    cont += 1
    if valor > 1000:
        maismil += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    while resp not in 'SN':
        resp = str(input('Quer continuar comprando? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do Programa'))
print(f'O total gasto foi de {totalG:.2f}')
print(f'No total tivemos {maismil} produtos mais caro que R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
