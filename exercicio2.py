nomeUsuario = input('Digite um nome para o seu usuário: ')
senha = input('Digite a senha para o seu usuário: ')

while nomeUsuario == senha:
    print('Usuário e senha não pode possuir os mesmos valores!')
    senha = input('Digite a senha para o seu usuário: ')

print('Usuário e senha definidos com sucesso!')