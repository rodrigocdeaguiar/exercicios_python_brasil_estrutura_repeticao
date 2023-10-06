quantidadeCds = int(input("Digite a quantidade de CD's da sua coleção: "))
somaGastosCds = 0
contador = 0

while contador < quantidadeCds:
    valorCd = float(input('Digite o valor gasto no CD: '))
    somaGastosCds = somaGastosCds + valorCd
    contador+=1

mediaGastosCd = somaGastosCds/quantidadeCds

print(f'Média de gastos por CD: {mediaGastosCd:.2f}')