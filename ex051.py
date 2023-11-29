'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''
print('=' * 25)
print('10 TERMOS DE UMA PA')
print('=' * 25)
p1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
d10 = p1 + (10 - 1) * r
for c in range(p1, d10 + 1, r):
    print(c, end = ' - ')
print('FIM')