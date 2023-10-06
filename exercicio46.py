cadastrarAtletas = True

while cadastrarAtletas == True:
    saltos = []
    atleta = input('Atleta: ')
    somaSaltos = 0
    contagem = 0
    primeiroSalto = float(input('Primeiro Salto: '))
    saltos.append(primeiroSalto)
    segundoSalto = float(input('Segundo Salto: '))
    saltos.append(segundoSalto)
    terceiroSalto = float(input('Terceiro Salto: '))
    saltos.append(terceiroSalto)
    quartoSalto = float(input('Quarto Salto: '))
    saltos.append(quartoSalto)
    quintoSalto = float(input('Quinto Salto: '))
    saltos.append(quintoSalto)
    for k in saltos:
        somaSaltos = somaSaltos + k
        if contagem == 0:
            maiorSalto = k
            menorSalto = k
        elif contagem !=0:
            if k > maiorSalto:
                maiorSalto = k
            if k < menorSalto:
                menorSalto = k
        contagem+=1
    somaSaltosRecalc = somaSaltos - maiorSalto - menorSalto
    media = somaSaltosRecalc/3
    print(f'Atleta: {atleta}\n'
          f'Melhor Salto: {maiorSalto} m\n'
          f'Pior Salto: {menorSalto} m\n'
          f'Média: {media:.1f} m')
    encerrarCadastroAtletas = input('Deseja encerrar a digitação de notas? Digite "SIM" ou qualquer tecla para continuar: ')
    if encerrarCadastroAtletas.lower() == 'sim':
        cadastrarAtletas = False
    else:
        continue