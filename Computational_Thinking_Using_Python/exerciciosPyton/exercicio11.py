salarioAntigo = float(input("Insira seu salario antigo "))
salarioNovo = float(input("Insira seu novo salario "))

diferença = salarioNovo - salarioAntigo
percentualDeAumento = (diferença / salarioAntigo) * 100

print(f"O percentual de aumento foi {percentualDeAumento}")