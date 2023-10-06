numeroUm = int(input('Digite um número inteiro: '))
numeroDois = int(input('Digite outro número inteiro: '))
soma = 0
if numeroUm < numeroDois:
    while numeroUm < (numeroDois-1):
        numeroUm +=1
        soma = soma+numeroUm
if numeroUm > numeroDois:
    while (numeroUm-1) > (numeroDois):
        numeroDois += 1
        soma = soma + numeroDois

print(soma)