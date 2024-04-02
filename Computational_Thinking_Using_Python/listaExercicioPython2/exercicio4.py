time1 = input("Qual o nome do primeiro time? ")
pontos1 = input("Quantos gols foram marcados? ")
time2 = input("QUal o nome do segundo time? ")
pontos2 = input("Quantos gols foram marcados? ")
p1 = int(pontos1)
p2 = int(pontos2)

if p1 > p2:
    print("o ", time1, " ganhou")
elif p2 > p1:
    print("o ", time2, " ganhou")
else:
    print("deu empatekkkkkk")
    
