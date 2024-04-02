import math
numero = int(input("coloque seu numero "))
raiz = math.sqrt(numero)

if raiz < 0: 
 print(f"impossivel calcular a raiz quadrada de {raiz}")

else:
 print(f"a raiz quadrada de {numero} é {raiz}")