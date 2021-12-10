#def nomedafuncao()
"""
def soma(num1, num2):
    num1 = 6
    num2 = 5
    total = num1 + num2
    return total

print(soma(num1,num2))
"""

"""
def soma(num1, num2):
    total = num1 + num2
    return total

valores = soma(5,6)

print(valores)
"""

"""
def operacao(num1, num2):
    soma = num1 + num2
    mult = num1 * num2
    return soma, mult
a,b = operacao(2,3)
print(a,b)
"""

#maneira mais "inteligênte de fazer"
"""
def operacao(num1, num2):
    #soma = num1 + num2
    return num1+num2, num1*num2
a,b = operacao(2,3)
print(a,b)
"""

"""
def soma(*lista): #o "*" indica vários parâmetros possíveis
    soma_num = 0
    print(lista)

    for num in lista:
        soma_num += num
    
    return soma_num


a = (1,2,3,4)
print(soma(1,2,3,4))
"""

#variáveis globais
x = 10

def incrementa():
    global x
    incremento = 5
    x += incremento

incrementa()
print(x)
