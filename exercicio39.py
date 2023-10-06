
for numeroAluno in range(1, 11):
    print(f'Aluno {numeroAluno}')
    alturaAluno = float(input('Digite a altura do aluno: '))
    if numeroAluno == 1:
        maiorAltura = alturaAluno
        alunoMaisAlto = numeroAluno
        menorAltura = alturaAluno
        alunoMaisBaixo = numeroAluno
    else:
        if alturaAluno > maiorAltura:
            maiorAltura = alturaAluno
            alunoMaisAlto = numeroAluno
        elif alturaAluno < menorAltura:
            menorAltura = alturaAluno
            alunoMaisBaixo = numeroAluno

print(f'Aluno mais alto: {alunoMaisAlto} ({maiorAltura} m)\n'
      f'Aluno mais baixo: {alunoMaisBaixo} ({menorAltura} m)')