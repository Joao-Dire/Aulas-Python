preco = float(input("Qual o preço do produto? "))
desconto = float(input("Qual o valor de desconto? "))
valorDesconto = (preco * desconto) / 100
valorNovo = preco - valorDesconto

print("o valor com o desconto é ", valorNovo)