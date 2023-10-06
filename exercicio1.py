nota = input('Digite o valor da nota entre 0 e 10: ')

while not nota.isdigit() or float(nota) > 10 or float(nota) < 0:
    nota = input('Digite o valor da nota entre 0 e 10: ')

print(nota)