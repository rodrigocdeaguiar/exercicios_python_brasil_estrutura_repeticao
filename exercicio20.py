qtdeCalculos = int(input('Digite a quantidade de números que terão os seus fatoriais calculados: '))

for k in range(0,qtdeCalculos):
    numero = int(input('Digite um número para saber o seu fatorial: '))
    resultado = 0
    while numero > 0:
        if resultado == 0:
            resultado = numero * (numero - 1)
            numero -= 2
        else:
            resultado = resultado * numero
            numero -= 1
    print(resultado)

print('Fim!')