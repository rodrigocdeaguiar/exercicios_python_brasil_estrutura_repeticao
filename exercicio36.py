valorTabuada = int(input('Digite o número a ser realizada a tabuada: '))
valorInicial = int(input('Digite o começo da tabuada: '))
valorFinal = int(input('Digite o final da tabuada: '))

print(f'Montar a tabuada de: {valorTabuada}\n'
      f'Começar por {valorInicial}\n'
      f'Terminar por {valorFinal}\n'
      f'')

for k in range(valorInicial, (valorFinal+1)):
     resultado = valorTabuada*k
     print(f'{valorTabuada}X{k} = {resultado}')