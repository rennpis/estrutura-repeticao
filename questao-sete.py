# 7) Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora.

# Armazenanamento dos dados
usuarios = []

# Loop de cadastro
while True:
    # Solicita os dados do usuário
    nome = input("Insira o nome do usuário ou 'cancelar' para cancelar o cadastro: ")
    
    # Verificação de cadastro
    if nome.lower() == "cancelar":
        break
    
    idade = int(input("Insira a idade do usuário: "))
    email = input("Insira o e-mail do usuário: ")
    print('')
    
    # Criação de dicionário de cadastros
    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }
    
    # Adicionando o usuário na lista com todos os usuários
    usuarios.append(usuario)

# Exibição de todos os usuários cadastrados
print("Usuários cadastrados:")
for usuario in usuarios:
    print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}, E-mail: {usuario['email']}")