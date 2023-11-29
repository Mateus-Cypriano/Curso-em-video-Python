from datetime import date
ano = int(input('Qual o ano deseja analizar? Digite 0 para calcular o ano atual: '))
if ano == 0:
    ano = date.today().year#modulo datetime. importa somente o ano do dia atual configurado no computador.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #calculo para verificar se um ano é bissexto. Ele tem que ser divísel por 4 e não por 100, exceto os anos que também forem divisiveis por 400.
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))
