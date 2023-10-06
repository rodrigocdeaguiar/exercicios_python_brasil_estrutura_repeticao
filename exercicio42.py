coletaNumeros = True
contZeroVinteCinco = 0
contVinteseisCinquenta = 0
contCinquentaeumSetentaecinco = 0
contSetentaeseisCem = 0
contadorGeral = 0


while coletaNumeros==True:
    if contadorGeral == 0:
        numero = int(input('Digite um número: '))
    elif contadorGeral != 0:
        numero = int(input('Digite outro número: '))
    if 0 <= numero <= 25:
        contZeroVinteCinco+=1
        contadorGeral+=1
    elif 26 <= numero <= 50:
        contVinteseisCinquenta+=1
        contadorGeral += 1
    elif 51 <= numero <= 75:
        contCinquentaeumSetentaecinco+=1
        contadorGeral += 1
    elif 76 <= numero <= 100:
        contSetentaeseisCem+=1
        contadorGeral += 1
    elif numero > 100:
        continue
    elif numero < 0:
        coletaNumeros = False

print()

from tabulate import tabulate

estrutura = {
    'Intervalos': ['[0-25]', '[26-50]', '[51-75]', '[76-100]'],
    'Quantidade': [contZeroVinteCinco, contVinteseisCinquenta, contCinquentaeumSetentaecinco, contSetentaeseisCem]
}

print('Tabela de intervalos dos números digitados:')
print(tabulate(estrutura, headers='keys', tablefmt='github' ))