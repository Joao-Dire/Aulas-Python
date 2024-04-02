n = int(input("Digite um numero inteiro positivo: "))
print (f"divisores de {n}: ")
    
divisor = 1 #contador

while n <= 0:
     print("Formato invalido, insira um numero inteiro positivo:")
     n = int(input("Digite um numero inteiro positivo: "))  
    
while divisor <= n:
        if n % divisor == 0:
            print(divisor)
        divisor += 1
    
    








