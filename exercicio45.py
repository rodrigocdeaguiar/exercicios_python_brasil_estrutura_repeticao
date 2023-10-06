correcaoProva = True
gabaritoProva = ['a', 'b', 'c', 'd', 'e', 'e', 'd', 'c', 'b', 'a']
contadorAlunos = 0
somaAcertos = 0

while correcaoProva == True:
    nomeAluno = input('Digite o nome do aluno: ')
    acertoAluno = 0
    questaoUm = input('Digite a letra marcada na questão 01: ')
    if questaoUm.lower() == gabaritoProva[0]:
        acertoAluno+=1
    questaoDois = input('Digite a letra marcada na questão 02: ')
    if questaoDois.lower() == gabaritoProva[1]:
        acertoAluno+=1
    questaoTres = input('Digite a letra marcada na questão 03: ')
    if questaoTres.lower() == gabaritoProva[2]:
        acertoAluno+=1
    questaoQuatro = input('Digite a letra marcada na questão 04: ')
    if questaoQuatro.lower() == gabaritoProva[3]:
        acertoAluno+=1
    questaoCinco = input('Digite a letra marcada na questão 05: ')
    if questaoCinco.lower() == gabaritoProva[4]:
        acertoAluno+=1
    questaoSeis = input('Digite a letra marcada na questão 06: ')
    if questaoSeis.lower() == gabaritoProva[5]:
        acertoAluno+=1
    questaoSete = input('Digite a letra marcada na questão 07: ')
    if questaoSete.lower() == gabaritoProva[6]:
        acertoAluno+=1
    questaoOito = input('Digite a letra marcada na questão 08: ')
    if questaoOito.lower() == gabaritoProva[7]:
        acertoAluno+=1
    questaoNove = input('Digite a letra marcada na questão 09: ')
    if questaoNove.lower() == gabaritoProva[8]:
        acertoAluno+=1
    questaoDez = input('Digite a letra marcada na questão 10: ')
    if questaoDez.lower() == gabaritoProva[9]:
        acertoAluno+=1
    somaAcertos+=acertoAluno
    if contadorAlunos == 0:
        maiorAcerto = acertoAluno
        alunoMaiorAcerto = nomeAluno
    elif contadorAlunos !=0:
        if acertoAluno > maiorAcerto:
            maiorAcerto = acertoAluno
            alunoMaiorAcerto = nomeAluno
    contadorAlunos+=1
    encerrarCadastro = input('Deseja encerrar a digitação de notas? Digite "SIM" ou qualquer tecla para continuar: ')
    if encerrarCadastro.lower() == 'sim':
        correcaoProva = False
    else:
        continue

mediaAcertos = somaAcertos/contadorAlunos

print()

print(f'Média de acertos: {mediaAcertos}\n'
      f'Total de alunos: {contadorAlunos}\n'
      f'Aluno com maior quantidade de acertos: {alunoMaiorAcerto}, {maiorAcerto} acertos.')