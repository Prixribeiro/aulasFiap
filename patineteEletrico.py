print("Este programa calcula a velocidade média de um patinete elétrico.")
distancia=float(input("Qual foi a distância percorrida pelo patinete? "))
tempo = float(input("Quantos minutos o patinete demorou para percorrer essa distância? "))
vel_media=distancia/tempo
print("O patinete atingiu a velocidade média de {0:.2f} m/min".format(vel_media))