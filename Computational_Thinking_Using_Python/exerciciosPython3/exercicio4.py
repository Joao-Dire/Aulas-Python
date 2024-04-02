def contar_positivos_negativos(sequencia):
    positivos = 0
    negativos = 0
    
    for numero in sequencia:
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
    
    print("Quantidade de números positivos:", positivos)
    print("Quantidade de números negativos:", negativos)

# Exemplo de uso:
n = 5  # Tamanho da sequência
sequencia = [2, -3, 4, -1, 0]
contar_positivos_negativos(sequencia)
