def impar_ou_par():
    sair = 0
    while sair != 'S':
        idade = int(input('digite sua idade: '))
        sair = (input('Sair? S/N: '))

        if idade%2 == 0:
            print('Sua idade é par')
            
        else:
            print('Sua idade é impar')
            
op = impar_ou_par()