anoInicial = 1995
salarioInicial = float(input('Digite o salário inicial: '))
anoAtual = int(input('Digite o ano atual: '))
percentualAumento = 0.015
salarioAtual = salarioInicial

for ano in range(anoInicial, (anoAtual+1)):
    if ano == 1995:
        aumento = 0
        salarioAtual = salarioInicial + aumento
    elif ano == 1996:
        aumento = salarioInicial*percentualAumento
        salarioAtual = salarioInicial+aumento
    else:
        percentualAumento = percentualAumento*2
        aumento = salarioAtual*percentualAumento
        salarioAtual = salarioAtual+aumento

print(f'Ano de entrada na empresa: {anoInicial}\n'
      f'Salário inicial: R${salarioInicial:.2f}\n'
      f'Ano atual: {anoAtual}\n'
      f'Salário atual: R${salarioAtual:.2f}')