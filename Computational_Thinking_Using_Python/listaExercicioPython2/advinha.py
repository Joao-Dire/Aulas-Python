import random

sorteado = random.randint(1, 1000)
print(sorteado)

chute = int(input("chute seu numero"))
tentativas = 10

if sorteado > chute:
    print("é menor!")

elif sorteado > chute:
    print("é maior!")

elif sorteado == chute:
    print("Acertou!")
    quit()

if tentativas >

