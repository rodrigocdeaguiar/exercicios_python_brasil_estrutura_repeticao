contagemGeral = 0
contagemPares = 0
contagemImpares = 0

for k in range(0,10):
    numero = int(input('Digite um número para saber se é par ou impar: '))
    contagemGeral +=1
    if numero%2 ==0:
        contagemPares+=1
    else:
        contagemImpares+=1

print(f'Números pares: {contagemPares}')
print(f'Números ímpares: {contagemImpares}')