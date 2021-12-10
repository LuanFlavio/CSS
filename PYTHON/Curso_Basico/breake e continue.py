"""
for i in range(10):
    if i == 5:
        break
    print(i)


for i in range(10):
    if i == 5:
        continue
    print(i)
"""

def criaLista():
    lista = []

    m = int(input("Digite o tamanho da lista: "))

    for i in range(m):
        ele = float(input("Digite o elemento %i de %i: "%(i+1,m)))
        lista.append(ele)

    return lista

def main():
    ll = criaLista()

    n = int(input("Digite o número de elementos que deseja somar: "))

    soma = 0
    for i in range(len(ll)):
        if i == n:
            break
        soma += ll[i]

    print("A soma é: ", soma)

main()
