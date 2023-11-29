nome=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('seu nome com letras maisculas é:')
print(nome.upper())
print('Seu nome ocm letras minusculas é:')
print(nome.lower())
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))#o primeiro espaço vai ter indice igual ao número de letras. ao acha-lo, achamos a quantidade de letras
