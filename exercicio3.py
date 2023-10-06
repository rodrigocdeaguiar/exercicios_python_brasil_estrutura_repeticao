nome = input('Digite um nome maior que três dígitos: ')

while len(nome) < 3:
    print('Nome inválido.')
    nome = input('Digite um nome maior que três dígitos: ')

print('Nome válido!')

idade = input('Digite um valor válido para a idade: ')

while not 0<=int(idade)<=150:
    print('Idade inválida.')
    idade = input('Digite um valor válido para a idade: ')

print('Idade válida!')

salario = input('Digite um valor válido para o salário, em R$: ')

while not salario.isdigit() and float(salario)<0:
    print('Salário inválido.')
    salario = input('Digite um valor válido para o salário, em R$: ')

print('Salário válido!')
salario = float(salario)

sexo = input('Escolha o sexo: M-Masculino ou F-Feminino: ')

while not (sexo.lower() == 'm' or sexo.lower() == 'f'):
    print('Sexo inválido.')
    sexo = input('Escolha o sexo: M-Masculino ou F-Feminino: ')

print('Sexo válido!')

estadoCivil = input('Escolha o estado civil: S-Solteiro, C-Casado, D-Divorciado ou V-Viúvo: ')

while not (estadoCivil.lower() == 's' or estadoCivil.lower() == 'c' or estadoCivil.lower() == 'd' or estadoCivil.lower() == 'v'):
    print('Estado civil inválido.')
    estadoCivil = input('Escolha o estado civil: S-Solteiro, C-Casado, D-Divorciado ou V-Viúvo: ')

print('Estado civil válido!')

print(f'{nome}, {idade} anos, salário de R${salario:.2f}, sexo {sexo}, estado civil {estadoCivil}.')