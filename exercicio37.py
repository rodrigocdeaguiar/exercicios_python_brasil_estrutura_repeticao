proximaPergunta = True
contador = 0
menorPeso = 0
maiorPeso = 0
menorAltura = 0
maiorAltura = 0
somaAlturas = 0
somaPesos = 0

while proximaPergunta == True:
    codigoCliente = input('Digite o código do cliente: ')
    peso = float(input('Digite o peso do cliente: '))
    altura = float(input('Digite a altura do cliente: '))
    if contador == 0:
        menorPeso = peso
        clienteMenosPesado = codigoCliente
        maiorPeso = peso
        clienteMaisPesado = codigoCliente
        menorAltura = altura
        clienteMenosAlto = codigoCliente
        maiorAltura = altura
        clienteMaisAlto = codigoCliente
        somaPesos = somaPesos + peso
        somaAlturas = somaAlturas + altura
        contador+=1
    else:
        if peso > maiorPeso:
            maiorPeso = peso
            clienteMaisPesado = codigoCliente
            somaPesos = somaPesos + peso
            contador += 1
        elif peso < menorPeso:
            menorPeso = peso
            clienteMenosPesado = codigoCliente
            somaPesos = somaPesos + peso
            contador += 1
        else:
            somaPesos = somaPesos + peso
            contador += 1

        if altura > maiorAltura:
            maiorAltura = altura
            clienteMaisAlto = codigoCliente
            somaAlturas = somaAlturas + altura
        elif altura < menorAltura:
            menorAltura = altura
            clienteMenosAlto = codigoCliente
            somaAlturas = somaAlturas + altura
        else:
            somaAlturas = somaAlturas + altura
    perguntaContinuidade = input('Deseja registrar um próximo cliente? Digite SIM para continuar, ou qualquer dígito para encerrar. ')
    if perguntaContinuidade == 'sim'.lower():
        proximaPergunta = True
    else:
        proximaPergunta = False

mediaAltura = somaAlturas/contador
mediaPeso = somaPesos/contador

print(f'Média de altura: {mediaAltura:.1f} m\n'
      f'Média de pesos: {mediaPeso:.1f} kg\n'
      f'Cliente mais alto: {clienteMaisAlto} ({maiorAltura} m )\n'
      f'Cliente mais baixo: {clienteMenosAlto} ({menorAltura} m)\n'
      f'Cliente mais gordo: {clienteMaisPesado} ({maiorPeso} kg)\n'
      f'Cliente mais magro: {clienteMenosPesado} ({menorPeso} kg)\n'
      f'')