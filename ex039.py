'''Crie um programa que leia o ano de nascimento de um garoto e informe, de acordo com a sua idade se ele ainda vai
se alistar no serviço militar, se é a hora exata para se alistar ou se já passou da hora.
O programa também deve mostrar o tempo que falta ou que passou do prazo'''

from datetime import date
nascimento = int(input('Em que ano você nasceu? '))
ano = date.today().year
if ano - nascimento == 18:
    print('\033[1;33mEstá na hora de se alistar para o serviço militar. Não se esqueça!\033[m')
elif ano - nascimento < 18:
    print('Ainda não está na hora de se alistar! \033[1;34mFalta(m) {} ano(s)\033[m, fique tranquilo!'.format(18 - (ano - nascimento)))
else:
    print('Já passou da hora de se alistar! \033[1;31mVocê deveria ter se alistado há {} ano(s).\033[m Espero que não tenha deixado passar.'.format((ano - nascimento) - 18))
