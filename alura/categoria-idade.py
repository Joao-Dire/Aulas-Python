def categoria_idade():
    sair = 0
    while sair != 'N' or sair != 'n':
        idade = int(input('Digite sua idade: '))
        sair = input('Sair? S/N: ')
        
        if idade <=12:
            print('vc e crianca')
        
        elif idade <=18:
            print('vc e adolescente')
        
        elif idade > 18:
            print('vc e adulto')
    return sair
        
op = categoria_idade()