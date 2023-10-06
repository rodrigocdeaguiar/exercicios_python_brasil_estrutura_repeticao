quantidadeProdutos = 50
precoPao = 0.18
contador = 0
print('Padaria do Pão Passado no Saco - Tabela de preços:')
for k in range(1,(quantidadeProdutos+1)):
    valorTotal = k*precoPao
    print(f'{k} - R${valorTotal:.2f}')