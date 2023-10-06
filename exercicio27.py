numeroTurmas = int(input('Digite a quantidade de turmas: '))
contador = 0
totalAlunos = 0

while contador < numeroTurmas:
    numeroAlunos = 41
    while numeroAlunos > 40 or numeroAlunos < 0:
        numeroAlunos = int(input('Digite o número de alunos da turma: '))
        if numeroAlunos > 40:
            print('Turma excedente. Valor inválido.')
        elif numeroAlunos < 0:
            print('Valor inválido.')
    totalAlunos = totalAlunos + numeroAlunos
    contador +=1

mediaAlunos = totalAlunos/numeroTurmas

print(f'Média de alunos: {mediaAlunos:.2f}')