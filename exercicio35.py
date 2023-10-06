num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

if num1 < num2:
    numMenor = num1
    numMaior = num2
elif num1 == num2:
    print('Error!')
else:
    numMenor = num2
    numMaior = num1

print(f'São números primos entre {numMenor} e {numMaior}')

for j in range(numMenor, (numMaior+1)):
    contadorPrimo = 0
    for k in range(1, (j + 1)):
        if j % k == 0:
            contadorPrimo += 1
        else:
            continue
    if contadorPrimo == 2 or contadorPrimo == 1:
        print(j)






