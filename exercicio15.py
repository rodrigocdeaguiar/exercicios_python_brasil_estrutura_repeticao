termosFibonacci = int(input('Digite a quantidade de termos da sequência de Fibonacci: '))
termoAnterior = 0
termoPosterior = 1
numeroFibonacci = 0

for k in range(0, termosFibonacci):
    numeroFibonacci = termoAnterior + termoPosterior
    termoAnterior = termoPosterior
    termoPosterior = numeroFibonacci
    print(numeroFibonacci)