tamanhoPercurso = float(input("Qual o tamanho do percurso? (em metros) "))
tempoPercurso = float(input("Quanto tempo demorou? "))
velocidadeMs = tamanhoPercurso / tempoPercurso
velocidadeKm = velocidadeMs / 1000

print("a velocidade em M/S é ", velocidadeMs)
print("a velocidade em KM/h", velocidadeKm)