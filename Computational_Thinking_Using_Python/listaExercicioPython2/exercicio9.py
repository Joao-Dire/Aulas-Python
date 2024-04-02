num_a = float(input("A: "))
op = input("op: ")
num_b = float(input("B: "))

if op == '+':
    resultado = num_a + num_b  

elif op == '-':
    resultado = num_a - num_b

elif op == '*':
    resultado = num_a * num_b

elif op == '/':
    if num_a !=0:
        resultado = num_a / num_b
else:
    print("impossível dividir por 0")
    quit()
    
print("o resultado é", resultado) 