pedidoAndamento = True
qtdeCachorroquente = 0
qtdeBauruSimples = 0
qtdeBaurucomOvo = 0
qtdeHamburger = 0
qtdeCheesburger = 0
qtdeRefrigerante = 0

while pedidoAndamento == True:
    produto = input('Digite o código do produto abaixo:\n'
                        '100 - Cachorro Quente: R$ 18,00\n'
                        '101 - Bauru Simples: R$25,00\n'
                        '102 - Bauru com Ovo: R$28,00\n'
                        '103 - Hamburger: R$20,00\n'
                        '104 - Cheesburger: R$27,00\n'
                        '105 - Refrigerante: R$7,00\n'
                        '\n')

    quantidadeProduto = int(input('Digite a quantidade: '))
    if produto == '100':
        qtdeCachorroquente+=quantidadeProduto
    elif produto == '101':
        qtdeBauruSimples+=quantidadeProduto
    elif produto == '102':
        qtdeBaurucomOvo+=quantidadeProduto
    elif produto == '103':
        qtdeHamburger+=quantidadeProduto
    elif produto == '104':
        qtdeCheesburger+=quantidadeProduto
    elif produto == '105':
        qtdeRefrigerante+=quantidadeProduto
    else:
        continue
    perguntaEncerramento = input('Deseja encerrar? Digite "S" para SIM, ou qualquer outra tecla para continuar: ')
    if perguntaEncerramento.lower() == 's':
        pedidoAndamento = False
    else:
        continue

estrutura = {
    'Código:': [100, 101, 102, 103, 104, 105],
    'Especificação:': ['Cachorro-Quente', 'Bauru Simples', 'Bauru com Ovo', 'Hamburger', 'Cheesburger', 'Refrigerante'],
    'Preço unitário (R$)': [18,25,28,20,27,7],
    'Quantidade': [qtdeCachorroquente, qtdeBauruSimples, qtdeBaurucomOvo, qtdeHamburger, qtdeCheesburger, qtdeRefrigerante],
    'Preço (R$)': [qtdeCachorroquente*18, qtdeBauruSimples*25, qtdeBaurucomOvo*28, qtdeHamburger*20, qtdeCheesburger*27, qtdeRefrigerante*7]
}

from tabulate import tabulate
print()
print(tabulate(estrutura, headers='keys', tablefmt='github'))
print()
valorTotal = qtdeCachorroquente*18+qtdeBauruSimples*25+qtdeBaurucomOvo*28+qtdeHamburger*20+qtdeCheesburger*27+qtdeRefrigerante*7
print(f'Valor total: R$ {valorTotal:.2f}')