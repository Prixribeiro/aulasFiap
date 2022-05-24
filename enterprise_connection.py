'''O desafio será a criação de um ranking de criticidade de violações/vazamentos “breaches” de dados pessoais em serviços de internet, por meio dos critérios de dados comprometidos como senha, ajuda da senha, número do telefone, nomes, e-mail e data do vazamento.'''

americanas = ["24 de julho de 2019","senha", "ajuda de senha", "nome", "email"]
magazine_luiza = ["24 de julho de 2017","senha", "ajuda de senha", "nome", "email"]
submarino = ["01 de janeiro de 2017","nome", "email"]
flash = ["01 de janeiro de 2022","numero telefone"]
hurb = ["03 de Maio de 2020", "email", "numero telefone"]
youtube = ["18 de maio de 2015", "senha", "ajuda de senha"]
adobe=["15 de outubro de 2013", "email", "ajuda de senha", "senha","nome"]
animegame=["15 de fevereiro de 2020", "email", "nome"]
gmail=["15 de setembro de 2015", "senha","email", "ajuda de senha"]
canva=["09 de maio de 2019", "nome","email"]

lista=[americanas, magazine_luiza, submarino,flash, hurb,youtube,adobe,animegame,gmail, canva]
lista_vazou_senha=[]
lista_vazou_ajuda=[]
lista_vazou_telefone=[]
lista_vazou_nome=[]
lista_vazou_email=[]

def checarDados(nome, empresa, indice):
    for i in empresa:
        if i == "senha":
            lista_vazou_senha.append(nome)
            lista_vazou_senha.append(lista[indice])
            return("Empresa: {} \nDados Vazados: {}".format(nome,lista[indice]))
        elif i == "ajuda de senha":
            lista_vazou_ajuda.append(nome)
            lista_vazou_ajuda.append(lista[indice])
            return ("Empresa: {} \nDados Vazados: {}".format(nome, lista[indice]))
        elif i == "numero telefone":
            lista_vazou_telefone.append(nome)
            lista_vazou_telefone.append(lista[indice])
            return ("Empresa: {} \nDados Vazados: {}".format(nome, lista[indice]))
        elif i == "nome":
            lista_vazou_nome.append(nome)
            lista_vazou_nome.append(lista[indice])
            return ("Empresa: {} \nDados Vazados: {}".format(nome, lista[indice]))
        elif i == "email":
            lista_vazou_email.append(nome)
            lista_vazou_email.append(lista[indice])
            return ("Empresa: {} \nDados Vazados: {}".format(nome, lista[indice]))


checarDados("Americanas",americanas,0)
checarDados("Magalu", magazine_luiza,1)
checarDados("Submarino", submarino,2)
checarDados("Flash", flash,3)
checarDados("Hurb", hurb,4)
checarDados("Youtube", youtube,5)
checarDados("Adobe", adobe,6)
checarDados("AnimeGame", animegame,7)
checarDados("Gmail", gmail,8)
checarDados("Canva", canva,9)

print("Vazou senha: ", lista_vazou_senha)
print("Vazou ajuda de senha: ",lista_vazou_ajuda)
print("Vazou nº de telefone: ",lista_vazou_telefone)
print("Vazou nome de usuário: ",lista_vazou_nome)
print("Vazou endereço de e-mail: ",lista_vazou_email)

