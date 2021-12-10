n = int(input("Digite o numero de elementos da lista: "))

lista = []
auxiliar = []

for i in range(n):
    elemento = int(input("Digite o elemento %i de %i: " %(i + 1,n)))
    lista.append(elemento)
    auxiliar.append(elemento)

print(lista)

for ele in auxiliar:
    aparicoes = lista.count(ele)
    for i in range(aparicoes-1):
        lista.remove(ele)
        
print(lista)
