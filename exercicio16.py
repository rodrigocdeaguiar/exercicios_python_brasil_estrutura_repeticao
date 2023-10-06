termoAnterior = 0
termoPosterior = 1
numeroFibonacci = 0

while numeroFibonacci < 500:
    numeroFibonacci = termoAnterior + termoPosterior
    termoAnterior = termoPosterior
    termoPosterior = numeroFibonacci
    print(numeroFibonacci)