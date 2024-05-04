def calcula_media(dados):
    soma = 0
    for nota in dados:
        soma = soma + nota
        return soma / len(dados)
    
n = int(input("Qtd de alunos: \n"))
lista_notas = []

contador = 0
while contador < n:
    nota = float(input("informe a nota: \n"))
    lista_notas.append(nota)
    contador = contador + 1

print(lista_notas)