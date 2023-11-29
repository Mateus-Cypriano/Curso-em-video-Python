sal = float(input('Digite o salário do funcionário: '))
if sal > 1250.0:
    nsal = sal + sal * 10/100 #calculando 10% de aumento no salário do funcionário.
    print('O aumento do funcionário será de: R${} Seu novo salário é R${}'.format(sal * 10/100, nsal))
else:
    nsal = sal + sal * 15/100
    print('O aumento do funcionário será de:R${} Seu novo salário é R${}'.format(sal * 15/100, nsal))
