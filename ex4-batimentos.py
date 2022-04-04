'''Verificar  se  os  batimentos  cardíacos  por  minuto  se  encontram  na  faixa adequada.
Para  isso,  você  deve  solicitar ao  usuário que informe  o  seu  número  de BATIMENTOS POR MINUTO (BPM)
e a IDADE. A partir disso,o script deveverificar e  exibir  uma  mensagem  informando  se  os  batimentos  do
usuário  encontram-se DENTRO  da  faixa  adequada,  ACIMA  da  faixa  adequada  ou  ABAIXO  da  faixa adequada,
de acordo com o site Tua Saúde'''

bpm = int(input("Informe  o  seu  número  de BATIMENTOS POR MINUTO (BPM): "))
idade = int(input("Informe sua idade: "))

if idade <= 2:
    if bpm >= 120 and  bpm <=140:
        print(" Batimentos dentro da faixa adequada!")
    elif bpm < 120:
        print("Batimentos abaixo da faixa adequada!")
    elif bpm > 140:
        print("Batimentos acima da faixa adequada!")
elif idade >=8 and idade <=17:
    if bpm >=80 and bpm <=100:
        print("Batimentos dentro da faixa adequada!")
    elif bpm < 80:
        print("Batimentos abaixo da faixa adequada!")
    elif bpm > 100:
        print("Batimentos acima da faixa adequada!")
elif idade >=18 and idade <=60:
    if bpm >= 70 and bpm <=80:
        print("Batimentos dentro da faixa adequada!")
    elif bpm <70:
        print("Batimentos abaixo da faixa adequada!")
    elif bpm > 80:
        print("Batimentos acima da faixa adequada!")
elif idade >= 60:
    if bpm >=50 and bpm <= 60:
        print("Batimentos dentro da faixa adequada!")
    elif bpm < 50:
        print("Batimentos abaixo da faixa adequada!")
    elif bpm > 60:
        print("Batimentos acima da faixa adequada!")
else:
    print("Para mais informações, confira o link em: https://www.tuasaude.com/frequencia-cardiaca/#:~:text=At%C3%A9%202%20anos%20de%20idade,idosos%3A%2050%20a%2060%20bpm")