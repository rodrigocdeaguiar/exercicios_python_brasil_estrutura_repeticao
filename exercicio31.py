valorCompra = 1
contador = 0
somaCompras = 0

while valorCompra !=0:
    valorCompra = float(input('Digite o valor do produto: '))
    somaCompras = somaCompras + valorCompra
    contador+=1
    print(f'Produto {contador}: R${valorCompra}')

print(f'Valor total: R$ {somaCompras}')

valorRecebido = float(input('Digite o valor de recimento: '))
troco = valorRecebido - somaCompras

print(f'Valor recebido: R$ {valorRecebido:.2f}\n'
      f'Troco: R$ {troco:.2f}')
