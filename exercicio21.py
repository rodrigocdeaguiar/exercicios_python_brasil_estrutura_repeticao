numero = int(input('Digite um número para saber se ele é primo, ou não: '))
contadorPrimo = 0

for k in range(1,(numero+1)):
    if numero%k==0:
        contadorPrimo+=1
    else:
        continue

if contadorPrimo == 2:
    print(f'O número {numero} é um número primo.')
else:
    print(f'O número {numero} é um número composto.')