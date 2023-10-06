numeroTabuada = int(input('Digite um número para saber a sua tabuada: '))

print()

for k in range(1,11):
    resultado = k*numeroTabuada
    print(f'{k}X{numeroTabuada} = {resultado}')