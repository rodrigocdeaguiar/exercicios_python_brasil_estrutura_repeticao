contador = 1

while contador <= 5:
    numero = float(input('Digite um número válido: '))
    if contador == 1:
        maiorNumero = numero
    if numero > float(maiorNumero):
        maiorNumero = float(numero)
    contador +=1


print(maiorNumero)