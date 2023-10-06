numeroTermos = int(input('Número de termos: '))
contagem = 0
soma = 0

while contagem < numeroTermos:
    if contagem == 0:
        n = 1
    divisao = 1/n
    soma = soma+divisao
    contagem+=1
    n+=1

print(f'S={soma:.2f}')