numeroUm = int(input('Digite um número inteiro: '))
numeroDois = int(input('Digite outro número inteiro: '))

if numeroUm < numeroDois:
    while numeroUm < (numeroDois-1):
        numeroUm +=1
        print(numeroUm)
if numeroUm > numeroDois:
    while (numeroUm-1) > (numeroDois):
        numeroDois += 1
        print(numeroDois)
