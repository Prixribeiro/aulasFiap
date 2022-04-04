'''Hora  de  decidir!  Os  colaboradores  da  sua equipe  foram  sorteados  para ganhar um console
de última geração,cada um,em razão do bom desempenho que tiveram nos últimos projetos.
Por uma questão de logística, porém, a empresa pede que todos os cinco membros da equipe recebam o
mesmo aparelho. Crie um algoritmo em que o usuário possa digitar o voto de cada um dos 5 membros da equipe e,
 ao final, exiba qual foi o console escolhido e com quantos votos.As opções são: PLAYSTATION, XBOX e NINTENDO'''

voto1= input("Digite qual console quer ganhar: PLAYSTATION, XBOX e NINTENDO ").upper()
voto2= input("Digite qual console quer ganhar: PLAYSTATION, XBOX e NINTENDO ").upper()
voto3= input("Digite qual console quer ganhar: PLAYSTATION, XBOX e NINTENDO ").upper()
voto4= input("Digite qual console quer ganhar: PLAYSTATION, XBOX e NINTENDO ").upper()
voto5= input("Digite qual console quer ganhar: PLAYSTATION, XBOX e NINTENDO ").upper()

playstation = 0
xbox = 0
nintendo = 0

if voto1 == "PLAYSTATION":
    playstation = playstation + 1
elif voto1 == "XBOX":
    xbox = xbox + 1
elif voto1 == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("Digite uma opção válida!")

if voto2 == "PLAYSTATION":
    playstation = playstation + 1
elif voto2 == "XBOX":
    xbox = xbox + 1
elif voto2 == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("Digite uma opção válida!")

if voto3 == "PLAYSTATION":
    playstation = playstation + 1
elif voto3 == "XBOX":
    xbox = xbox + 1
elif voto3 == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("Digite uma opção válida!")

if voto4 == "PLAYSTATION":
    playstation = playstation + 1
elif voto4 == "XBOX":
    xbox = xbox + 1
elif voto4 == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("Digite uma opção válida!")

if voto5 == "PLAYSTATION":
    playstation = playstation + 1
elif voto5 == "XBOX":
    xbox = xbox + 1
elif voto5 == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("Digite uma opção válida!")

if playstation > xbox and playstation > nintendo:
    print("O console escolhido foi o Playstation, com um total de {} votos.".format(playstation))
elif xbox > playstation and xbox > nintendo:
    print("O console escolhido foi o XBOX, com um total de {} votos.".format(xbox))
elif nintendo > xbox and nintendo > playstation:
    print("O console escolhido foi o Nintendo, com um total de {} votos.".format(nintendo))
else:
    print("Houve um empate, todos votam novamente!")