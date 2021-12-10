"""
lista = [1,2,3,4]

print(lista[0])
"""

"""
lista = [1,2,3,4]

for i in range(4):
    print(lista[i])
"""

"""
cesta = ["Banana","Maçã","Uva","Tomate"]

for i in range(4):
    print(cesta[i])
"""

"""
cesta = ["Banana","Maçã","Uva","Tomate"]

#for i in range(4):
print(cesta[-1]) #valor negativo vai de trás para frente
"""

"""
cesta = ["Banana","Maçã",["Uva","Tomate"]]

#for i in range(4):
print(cesta[2][1]) #busca item de uma lista dentro de outra
print(len(cesta))
"""

lista = []
num = int(input("Digite um valor: "))

while num!= -1:
    lista.append(num)
    num = int(input("Digite um valor: "))

elemento = int(input("Qual valor a ser procurado: "))

cont = 0

for i in range(len(lista)):
    if lista[i] == elemento:
        cont += 1

print("O elemento %i aparece %i vezes na sequência." %(elemento, cont))
