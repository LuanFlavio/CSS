#programa para o banco usar, pois soma o saldo de todas contas
contas = []
depositos = []
saldo = 0

def main():
    opcao = bool(int(input("Deseja ver ou criar uma conta(1) ou fechar o programa(0): ")))
    while opcao:
        criarConta()
        verSaldo()
        opcao = bool(int(input("Deseja ver ou criar a conta(1) ou fechar o programa(0): ")))

def criarConta():
    global contas, depositos, saldo
    num_conta = int(input("Digite o número da conta: "))

    while num_conta in contas:
        print("Conta já existente. Digite novamente.")
        num_conta = int(input("Digite o número da conta: "))

    contas.append(num_conta)
    deposito = float(input("Digite o valor do primeiro deposito: "))
    while deposito <= 0:
        print("Valor do deposito invalido")
        deposito = float(input("Digite o valor do seu deposito: "))
    depositos.append(deposito)
    saldo += deposito

def verSaldo():
    global saldo
    opcao = bool(int(input("Deseja ver o saldo do banco(1 - Sim / 0 - Não): ")))
    if opcao:
        print("O saldo do banco é R$", saldo)

main()
