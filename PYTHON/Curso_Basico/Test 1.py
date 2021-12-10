nomes = {
        "name": "Luan",
        "age": 18,
        "country": "Brazil"

}
nomes["age"] = str(nomes["age"])
print(nomes["name"] + '\n' + nomes.get("age") + '\n' + nomes["country"])

        
def escolhas():
        options = input("""Qual a informação que deseja mudar?
1 - Nome
2 - Idade
3 - País
>""")
        
        if options == "1":
                nomes["name"] = input("Qual seu nome? ")
                main()

        elif options == "2":
                nomes["age"] = input("Qual sua idade? ")
                main()

        elif options == "3":
                nomes["country"] = input("Qual seu país? ")
                main()

        else:
                print("Digite um valor existente")
                escolhas()

def main():
        button = input("Quer trocar alguma informação?(S ou N) ")
        if button.upper() == "S":
                escolhas()
        else:
                print(f"Tenha um bom dia",nomes["name"],"!")

main()       
print(nomes)


