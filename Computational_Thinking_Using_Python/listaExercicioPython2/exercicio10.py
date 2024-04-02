import math
a = int(input("digite o valor de A "))
b = int(input("digite o valor de B "))
c = int(input("digite o valor de C ")) 

delta = b*b - (4 * a * c)

x1 = (-b + math.sqrt(delta)) / (2 * a)

x2 = (-b - math.sqrt(delta)) / (2 * a)

print("as suas raizes sao ", x1, x2)