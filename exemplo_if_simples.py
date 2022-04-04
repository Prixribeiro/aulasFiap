idade = int(input("Digite sua idade: "))
rm = input("Digite seu rm: ")

if idade >= 18:
    print("Sua participação foi autorizada, aluno de RM {}. \nMais informações serão enviadas em seu e-mail cadastrado na FIAP.".format(rm))
else:
    autorizacao = input("Você possui autorização dos pais e/ou responsáveis: Digite S para sim ou N para não: ")
    if autorizacao == "S":
        print("Sua participação foi autorizada, aluno de RM {}. \nMais informações serão enviadas para o email dos responsáveis cadastrado na FIAP.".format(rm))
    else:
        print("Sua participação não foi autorizada por ser menor de idade!")