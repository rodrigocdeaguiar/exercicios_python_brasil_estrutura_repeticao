numero = int(input('Digite um número para saber o seu fatorial: '))
resultado = numero


if numero == 1:
    print(f'{numero}! = ', end='')
else:
    print(f'{numero}! = ', end='')
    for k in range(numero, 0, -1):
        if resultado == k:
            resultado = resultado*1
            print(f'{k}.', end='')
        elif k == 1:
            resultado = resultado * 1
            print(f'{k}', end=' = ')
        else:
            resultado = resultado * k
            print(f'{k}.', end='')

print(resultado)