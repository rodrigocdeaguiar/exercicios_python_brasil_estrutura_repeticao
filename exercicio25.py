numeroPessoas = int(input('Digite o número de pessoas: '))
contador = 0
somaIdades = 0
while contador<numeroPessoas:
    idade = int(input('Digite a idade de uma das pessoas: '))
    somaIdades = somaIdades+idade
    contador+=1

mediaIdades = somaIdades/numeroPessoas

if 0 <= mediaIdades <= 25:
    print(f'Turma jovem. Média de idade: {mediaIdades:.2f} anos')
elif 26 <= mediaIdades <= 60:
    print(f'Turma Adulta. Média de idade: {mediaIdades:.2f} anos')
elif mediaIdades > 60:
    print(f'Turma Idosa. Média de idade: {mediaIdades:.2f} anos')
