numeroTermos = int(input('Número de termos: '))
contagem = 0
soma = 0

while contagem < numeroTermos:
    if contagem == 0:
        n = 1
        m = 1
    divisao = n/m
    soma = soma+divisao
    contagem+=1
    n+=1
    m+=2

print(f'S={soma:.2f}')