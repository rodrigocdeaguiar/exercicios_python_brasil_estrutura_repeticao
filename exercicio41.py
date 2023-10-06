

emprestimo = float(input('Digite o valor do empréstimo: '))

print()

dividaTresPrestacoes = emprestimo + emprestimo*0.1
dividaSeisPrestacoes = emprestimo + emprestimo*0.15
dividaNovePrestacoes = emprestimo + emprestimo*0.2
dividaDozePrestacoes = emprestimo + emprestimo*0.25

from tabulate import tabulate

estrutura = {
    'Valor da dívida (R$)': [emprestimo, dividaTresPrestacoes, dividaSeisPrestacoes, dividaNovePrestacoes, dividaDozePrestacoes],
    'Valor dos juros (R$)': [(emprestimo-emprestimo), dividaTresPrestacoes-emprestimo, dividaSeisPrestacoes-emprestimo, dividaNovePrestacoes-emprestimo, dividaDozePrestacoes-emprestimo],
    'Quantidade de parcelas': [1, 3, 6, 9, 12],
    'Valor da parcela (R$)': [emprestimo, ((dividaTresPrestacoes/3)), (dividaSeisPrestacoes/6), (dividaNovePrestacoes/9), (dividaDozePrestacoes/12)]
}

print(tabulate(estrutura, headers='keys', tablefmt='github'))

#Esse código é o primeiro utilizando a formatação em tabalas. Por isso, não consegui formatar as casas decimais, tampouco inserir a moeda antes do número