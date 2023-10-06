baseNumero = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))
resultado = 0

for k in range(0, expoente):
    if k==0:
        resultado = baseNumero*1
    else:
        resultado = resultado*baseNumero

print(resultado)