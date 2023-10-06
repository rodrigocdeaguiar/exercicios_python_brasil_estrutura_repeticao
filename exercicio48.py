numero = input('Digite um número inteiro positivo: ')
novonumero = ''
for k in numero:
    novonumero = k+novonumero
if novonumero.isdigit() and int(novonumero) > 0:
    novo = int(novonumero)
    print(novonumero)
else:
    print('ERROR!')