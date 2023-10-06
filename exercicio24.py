numeroNotas = int(input('Digite o número de notas que serão calculadas: '))
contador = 0
somaNotas = 0
while contador < numeroNotas:
    nota = float(input('Digite uma nota: '))
    somaNotas = somaNotas+nota
    contador+=1

media = somaNotas/numeroNotas
print(f'Média = {media:.1f}')