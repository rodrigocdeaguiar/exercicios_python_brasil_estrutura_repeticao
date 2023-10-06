numeroTermos = int(input('Digite a quantidade de números que serão analisados: '))
contador = 0
soma = 0
while contador < numeroTermos:
    numero = int(input('Digite um número inteiro: '))
    if numero < 0 or numero > 1000:
        print('Digite um número entre 0 e 1000: ')
        continue
    else:
        if contador == 0:
            menorValor = numero
            maiorValor = numero
            soma = soma + numero
        else:
            if numero > maiorValor:
                maiorValor = numero
            if numero < menorValor:
                menorValor = numero
                soma = soma + numero
        contador += 1

print(f'Menor valor: {menorValor}')
print(f'Maior valor: {maiorValor}')