n_alunos = int(input("Qual a quantidade de alunos? "))   #definir quantos alunos tem na sala
n_provas = 0    #usado para medir quantas notas tem no total
soma_notas = 0
notas_abaixo_de_5 = 0
notas_acima_de_5 = 0

while n_provas < n_alunos:
    notas = int(input(f"digite a nota do aluno numero {n_provas + 1}: "))
    soma_notas = soma_notas + notas  
    n_provas = n_provas + 1 
    
    print(f"O aluno {n_provas} tirou {notas}")
      
    if notas < 5:
        notas_abaixo_de_5 += 1
    elif notas >= 5:
        notas_acima_de_5 += 1


media = soma_notas / n_provas
print(f"a soma total das notas foi {soma_notas} ")

print(f"a media das notas foi {media}")

print(f"Alunos com notas abaixo de 5: {notas_abaixo_de_5}")

print(f"Alunos com notas acima ou igual a 5: {notas_acima_de_5}")

   