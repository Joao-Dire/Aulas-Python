import os

def exibir_programa():
    print('Sabor Express')
    print('1. Cadastrrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')


def finalizar_app(): 
    os.system('cls')
    print('Obrigado por utilizar o Sabor Express!')
     
def escolher():
    opcao = int(input('Selecione uma opcao: '))

    if opcao == 1:
        print('Insira o nome do seu restaurante')
            
    elif opcao == 2:
            print("Listar restaurantes")
            
    elif opcao == 3:
            print("Ativar restaurante")
    else:
        finalizar_app()
    return opcao

def main():
    exibir_programa()
    escolher()
if __name__ == '__main__':
    main()
        

    
