quantidadeProdutos = 50
precoProduto = 1.99
contador = 0
print('Loja da Putaria - Tabela de preços:')
for k in range(1,(quantidadeProdutos+1)):
    valorTotal = k*precoProduto
    print(f'{k} - R${valorTotal:.2f}')