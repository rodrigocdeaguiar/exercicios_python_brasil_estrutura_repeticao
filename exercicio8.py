contador = 1
soma = 0

while contador <= 5:
    numero = float(input('Digite um número válido: '))
    soma = soma + numero
    contador +=1
    print(numero)

media = soma / 5

print(f'Soma = {soma}, Média = {media:.2f}')