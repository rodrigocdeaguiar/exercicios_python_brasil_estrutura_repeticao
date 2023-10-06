atleta = input('Digite o nome do atleta: ')
contadorJurados = 7
somaNotas = 0

while contadorJurados > 0:
    notaJurado = float(input('Nota: '))
    if contadorJurados == 7:
        maiorNota = notaJurado
        menorNota = notaJurado
    else:
        if notaJurado > maiorNota:
            maiorNota = notaJurado
        if notaJurado < menorNota:
            menorNota = notaJurado
    somaNotas = somaNotas+notaJurado
    contadorJurados-=1

somaNotasRecalculada = somaNotas-maiorNota-menorNota
mediaPontuacao=somaNotasRecalculada/5

print(f'Resultado final\n'
      f'Atleta: {atleta}\n'
      f'Melhor nota: {maiorNota}\n'
      f'Pior nota: {menorNota}\n'
      f'Média: {mediaPontuacao}')