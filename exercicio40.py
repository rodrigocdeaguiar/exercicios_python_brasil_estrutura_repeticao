contadorGeral = 0
contadorCidadesPequenas = 0
somaVeiculos = 0
acidentesCidadesPequenas = 0
maiorIndiceAcidentes = 0
menorIndiceAcidentes = 0
cidadeMaiorIndiceAcidentes = ''
cidadeMenorIndiceAcidentes = ''
for k in range(1,11):
    codigoCidade = input('Digite o código da cidade: ')
    numeroVeiculos = int(input('Digite o número de veículos de passeio (em 1999): '))
    acidentesTransitoVitimas = int(input('Digite o número de acidentes de trânsito com vítimas (em 1999): '))
    percentualAcidentes = (acidentesTransitoVitimas/numeroVeiculos)*1000
    somaVeiculos = somaVeiculos + numeroVeiculos
    contadorGeral+=1
    if k == 1:
        maiorIndiceAcidentes = percentualAcidentes
        cidadeMaiorIndiceAcidentes = codigoCidade
        menorIndiceAcidentes = percentualAcidentes
        cidadeMenorIndiceAcidentes = codigoCidade
    else:
        if percentualAcidentes > maiorIndiceAcidentes:
            maiorIndiceAcidentes = percentualAcidentes
            cidadeMaiorIndiceAcidentes = codigoCidade
        elif percentualAcidentes < menorIndiceAcidentes:
            menorIndiceAcidentes = percentualAcidentes
            cidadeMenorIndiceAcidentes = codigoCidade
        else:
            continue
    if numeroVeiculos < 2000:
        contadorCidadesPequenas+=1
        acidentesCidadesPequenas = acidentesCidadesPequenas+acidentesTransitoVitimas

mediaVeiculos = somaVeiculos/contadorGeral
mediaAcidentesCidadesPequenas = acidentesCidadesPequenas/contadorCidadesPequenas

print(f'Maior índice de acidentes de trãnsito: {cidadeMaiorIndiceAcidentes} ({maiorIndiceAcidentes:.2f} a cada 1000 veículos)\n'
      f'Menor índice de acidentes de trãnsito: {cidadeMenorIndiceAcidentes} ({menorIndiceAcidentes:.2f} a cada 1000 veículos)\n'
      f'Média de veículos: {mediaVeiculos:.2f} por cidade\n'
      f'Média de acidentes de trânsito em cidades com menos de 2000 veículos: {mediaAcidentesCidadesPequenas:.2f}')