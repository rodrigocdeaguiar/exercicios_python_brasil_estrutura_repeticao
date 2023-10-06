registro = True
contador = 0
somaTemperaturas = 0
while registro == True:
    temperatura = float(input('Digite a temperatura: '))
    if contador == 0:
        maiorTemperatura = temperatura
        menorTemperatura = temperatura
        somaTemperaturas = somaTemperaturas + temperatura
        contador += 1
    else:
        if temperatura > maiorTemperatura:
            maiorTemperatura = temperatura
            somaTemperaturas = somaTemperaturas + temperatura
            contador += 1
        elif temperatura < menorTemperatura:
            menorTemperatura = temperatura
            somaTemperaturas = somaTemperaturas + temperatura
            contador += 1
        else:
            somaTemperaturas = somaTemperaturas + temperatura
            contador += 1
    novoRegistro = input('Deseja fazer um novo registro de temperatura? Digite "sim", ou qualquer dígito: ')
    if novoRegistro == 'sim'.lower():
        registro = True
    else:
        registro = False

mediaTemperaturas = somaTemperaturas / contador

print(f'Máxima: {maiorTemperatura:.1f}°C\n'
      f'Mínima: {menorTemperatura:.1f}°C\n'
      f'Média: {mediaTemperaturas:.1f}°C')