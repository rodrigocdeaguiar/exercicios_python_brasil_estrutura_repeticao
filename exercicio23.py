numero = int(input('Digite um número para saber se ele é primo, ou não: '))
contadorPrimo = 0
numeroTestes = 0

for k in range(1,(numero+1)):
    if numero%k==0:
        print(f'Resto da divisão = {numero}/{k} = {(numero%k):.2f}')
        contadorPrimo+=1
        numeroTestes+=1
    else:
        print(f'Resto da divisão = {numero}/{k} = {(numero%k):.2f}')
        numeroTestes += 1
        continue

if contadorPrimo == 2:
    print(f'O número {numero} é um número primo.')
    print(f'Foram realizados {numeroTestes} testes.')
else:
    print(f'O número {numero} é um número composto.')
    print(f'Foram realizados {numeroTestes} testes.')