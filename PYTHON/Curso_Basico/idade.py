idade = int(input("Digite sua idade: "))

if idade>=18:
    tem_filhos = input("Vc tem filhos? ")
    if tem_filhos == Sim or sim:
        filhos = int(input("Quantos filhos vc tem? "))
    elif tem_filhos == Não or não:
        print("Obrigado por ajudar na pesquisa!")
    else:
        print("Resposta inválida!")

else:
    print("Vc ainda não é responsável.")
