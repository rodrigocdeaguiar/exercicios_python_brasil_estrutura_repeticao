contadorGeralVotos = 0
votosCandidatoUm = 0
votosCandidatoDois = 0
votosCandidatoTres = 0
votosCandidatoQuatro = 0
votosNulo = 0
votosBranco = 0
codigoencerramento = 'chacrinha'

votacaoAberta = True

while votacaoAberta == True:
    voto = int(input('Digite o número do seu candidato/voto:\n'
                     '1: João Cornivaldo\n'
                     '2: Cafetão da Esquina\n'
                     '3: Joelma da FB\n'
                     '4: Tia Ivonete\n'
                     '5: Nulo\n'
                     '6: Branco\n'
                     '\n'))
    if voto == 1:
        contadorGeralVotos+=1
        votosCandidatoUm+=1
    elif voto == 2:
        contadorGeralVotos+=1
        votosCandidatoDois+=1
    elif voto == 3:
        contadorGeralVotos+=1
        votosCandidatoTres+=1
    elif voto == 4:
        contadorGeralVotos+=1
        votosCandidatoQuatro+=1
    elif voto == 5:
        contadorGeralVotos+=1
        votosNulo+=1
    elif voto == 6:
        contadorGeralVotos+=1
        votosBranco+=1
    else:
        continue
    encerrarVotacao = input('Deseja encerrar a votação? Digite qualquer tecla para continuar ou o código para encerrar: ')
    if encerrarVotacao.lower() == codigoencerramento:
        votacaoAberta = False
    else:
        continue

percentualCanditatoUm = votosCandidatoUm/contadorGeralVotos*100
percentualCanditatoDois = votosCandidatoDois/contadorGeralVotos*100
percentualCanditatoTres = votosCandidatoTres/contadorGeralVotos*100
percentualCanditatoQuatro = votosCandidatoQuatro/contadorGeralVotos*100
percentualNulos = votosNulo/contadorGeralVotos*100
percentualBrancos = votosBranco/contadorGeralVotos*100

estrutura = {
    'Código': [1,2,3,4,5,6],
    'Candidatos': ['João Cornivaldo','Cafetão da Esquina','Joelma da FB','Tia Ivonete','Nulo','Branco'],
    'Votos': [votosCandidatoUm,votosCandidatoDois,votosCandidatoTres,votosCandidatoQuatro,votosNulo,votosBranco],
    'Percentuais: ': [percentualCanditatoUm, percentualCanditatoDois, percentualCanditatoTres, percentualCanditatoQuatro, percentualNulos, percentualBrancos]
}

print()

from tabulate import tabulate

print(tabulate(estrutura, headers='keys', tablefmt='github'))

print(f'Total de votos válidos: {contadorGeralVotos}')