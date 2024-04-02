valor = float(input("Qual o valor do produto?"))
pagamento = int(input("qual condicao de pagamento? (1-4): "))

if pagamento == 1:
    valor = valor - valor * 0.1
    print(f"valor a ser pago: {valor} ")
elif pagamento == 2:
    valor = valor - valor * 0.05
    print(f"valor a ser pago: {valor} ")
elif pagamento == 3:
    valor = valor/2
elif pagamento == 4:
    valor = valor + valor * 0.07
    print(f"valor a ser pago por parcela: {valor} ")
else:
    print("forma de pagamento invalida")
    
    

