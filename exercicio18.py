numeroTermos = int(input('Digite a quantidade de números que serão analisados: '))
contador = 0
soma = 0
for k in range(0,numeroTermos):
    numero = int(input('Digite um número inteiro: '))
    if contador == 0:
        menorValor = numero
        maiorValor = numero
        soma = soma+numero
        contador +=1
    else:
        if numero > maiorValor:
            maiorValor = numero
        if numero < menorValor:
            menorValor = numero
        soma = soma+numero
        contador+=1

print(f'Menor valor: {menorValor}')
print(f'Maior valor: {maiorValor}')