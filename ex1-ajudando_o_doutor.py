nota_aluno = float(input("Digite sua nota do semestre: "))
email_aluno = input("Digite seu email: ")

if nota_aluno >= 8.5:
    print("ENVIANDO CONVITE PARA {}!".format(email_aluno))
else:
    print("Você não atingiu a nota necessária para participar da visita!")