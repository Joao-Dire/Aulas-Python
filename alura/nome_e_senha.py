def cadastrar():
    print("Cadastro de usuário")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    print("Login")
    confirma_nome = input("Digite seu nome: ")
    confirma_senha = input("Digite sua senha: ")

    if nome == confirma_nome and senha == confirma_senha:
        print("Login realizado com sucesso")
    else:
        print("Erro no login, tente novamente")
        
op = cadastrar()
