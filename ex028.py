#exercício de advinhação de número usuário X máquina.

import random
from time import sleep

n1 = random.randint(0, 5)
print('Estou pensando em um número entre 0 e 5.')
u = int(input('Em que número estou pensando? '))
print('PROCESSANDO...')
sleep(2)
if u == n1:
    print('É exatamente esse número. Parabéns!')
else:
    print('Que pena, eu pensei no número {} e não no número {}'.format(n1, u))


