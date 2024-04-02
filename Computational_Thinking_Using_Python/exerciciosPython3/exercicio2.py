n_alunos = int(input("Qual a quantidade de alunos? "))
n_provas = 0
soma_notas = 0

while n_provas < n_alunos:
    notas = int(input(f"digite a nota do aluno numero {n_provas + 1}: "))
    soma_notas = soma_notas + notas
    n_provas = n_provas + 1 
    print(f"O aluno {n_provas} tirou {notas}")

media = soma_notas / n_provas
print(f"a soma total das notas foi {soma_notas} ")
print(f"a media das notas foi {media}")


   