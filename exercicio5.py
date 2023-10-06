popPaisA = int(input('Informe a população do país A, em hab: '))
txCrescPaisA = float(input('Informe as taxa de crescimento populacional do país A, em %/anuais: '))
popPaisB = int(input('Informe a população do país B, em hab: '))
txCrescPaisB = float(input('Informe as taxa de crescimento populacional do país A, em %/anuais: '))
txCrescPaisA = txCrescPaisA/100
txCrescPaisB = txCrescPaisB/100
realizarNovamenteOperacao = 'sim'
anos = 0

while not realizarNovamenteOperacao.lower() == 'sim:':
    while not popPaisA == popPaisB:
        popPaisA = popPaisA + (popPaisA * txCrescPaisA)
        popPaisB = popPaisB + (popPaisB * txCrescPaisB)
        anos += 1
    print(anos)
    realizarNovamenteOperacao = input('Deseja realizar novamente a operação: Digite "SIM", ou qualquer comando para '
                                      'encerrar: ')
    if realizarNovamenteOperacao.lower() == 'sim':
        popPaisA = int(input('Informe a população do país A, em hab: '))
        txCrescPaisA = float(input('Informe as taxa de crescimento populacional do país A, em %/anuais: '))
        popPaisB = int(input('Informe a população do país B, em hab: '))
        txCrescPaisB = float(input('Informe as taxa de crescimento populacional do país A, em %/anuais: '))
        txCrescPaisA = txCrescPaisA / 100
        txCrescPaisB = txCrescPaisB / 100
        anos = 0
        continue
    else:
        break

print('Obrigado por utilizar o nosso aplicativo!')