totalEleitores = int(input('Digite o número total de eleitores: '))
contador = 0
TotalCandidatoUm = 0
TotalCandidatoDois = 0
TotalCandidatoTrês = 0
TotalNulos = 0
while contador < totalEleitores:
    candidato = int(input('Digite o número do seu candidato:\n'
                          '1 - Bucenilda\n'
                          '2 - Cornivaldo\n'
                          '3 - Rolantino\n'
                          ''))
    if candidato == 1:
        TotalCandidatoUm+=1
    elif candidato == 2:
        TotalCandidatoDois+=1
    elif candidato == 3:
        TotalCandidatoTrês+=1
    else:
        TotalNulos+=1
    contador+=1

print(f'Total de votos:\n'
      f'1 - Bucenilda: {TotalCandidatoUm}\n'
      f'2 - Cornivaldo: {TotalCandidatoDois}\n'
      f'3 - Rolantino: {TotalCandidatoTrês}\n'
      f'Votos Nulos: {TotalNulos}')