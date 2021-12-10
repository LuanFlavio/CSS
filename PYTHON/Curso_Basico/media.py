alunos = 8
medias = []

for i in range(1, alunos + 1):
    notas = 0
    for j in range(1, 5):
        notas += float(input("Digite a nota %i de 4 notas do aluno %i de %i: " %(j, i, alunos)))
    notas /= 4
    medias.append(notas)

num = 0

for media in medias:
    if media >= 6:
        num += 1
        
print("O número de alunos com média igual ou maior que 6 é(são) ", num)
