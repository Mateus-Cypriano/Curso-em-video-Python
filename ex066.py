s = cont = 0
while True:
    n = int(input('Digite um número: [999 para parar] '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'o total de números digitados foi de {cont} e a soma deles é igual a {s}')
print('Fim')
