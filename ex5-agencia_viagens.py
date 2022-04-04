'''Viajar  é  bom  demais!  Uma  agência  de  viagens  está  propondo  uma estratégia para
alavancar as vendas após os impactos da pandemia do coronavírus.
A   empresa   ofertará   descontos   progressivos   na   compra   de   pacotes, dependendo do número
de viajantes que estão no mesmo grupo e moram na mesma residência. Para  ajudar  a  tornar  esse  projeto  real,
você  deve  criar  um  algoritmo  que receba  o  VALOR  BRUTO  do  pacote,  a  CATEGORIA  DOS  ASSENTOS  no voo e
a QUANTIDADE  DE  VIAJANTES  que  moram  em  uma  mesma  casa  e  calcule  os descontos de acordo com a
tabela abaixo:'''

viajantes = int(input("Informe a quantidade de viajantes que residem na mesma casa: "))
voo = input("Qual a categoria do seu vôo? |Econômica| - |Executiva| - |Primeira Classe|: ").upper()
valor_bruto = float(input("Informe o valor total da viagem: "))

if viajantes == 1:
    print("Passageiros viajando sozinho não tem direito a nenhum desconto")
    print("O valor total da viagem é de R$ {0:.2f}".format(valor_bruto))

elif viajantes == 2:
    if voo == "ECONÔMICA":
        desconto = valor_bruto * 0.03
        valor_liquido = valor_bruto - desconto
        media_pax = valor_liquido/viajantes
    elif voo == "EXECUTIVA":
        desconto = valor_bruto * 0.05
        valor_liquido = valor_bruto - desconto
        media_pax = valor_liquido / viajantes
    elif voo == "PRIMEIRA CLASSE":
        desconto = valor_bruto * 0.10
        valor_liquido = valor_bruto - desconto
        media_pax = valor_liquido / viajantes

    print("O valor bruto da viagem é R$ {0:.2f}".format(valor_bruto))
    print("O valor total do desconto é de R$ {0:.2f}".format(desconto))
    print("O valor a ser pago com desconto é de R$ {0:.2f}".format(valor_liquido))
    print("O valor médio por passageiro é de R$ {0:.2f}".format(media_pax))

elif viajantes == 3:
    if voo == "ECONÔMICA":
        desconto = valor_bruto * 0.04
        valor_liquido = valor_bruto - desconto
        media_pax = valor_liquido/viajantes
    elif voo == "EXECUTIVA":
        desconto = valor_bruto * 0.07
        valor_liquido = valor_bruto - desconto
        media_pax = valor_liquido / viajantes
    elif voo == "PRIMEIRA CLASSE":
        desconto = valor_bruto * 0.15
        valor_liquido = valor_bruto - desconto
        media_pax = valor_liquido / viajantes

    print("O valor bruto da viagem é R$ {0:.2f}".format(valor_bruto))
    print("O valor total do desconto é de R$ {0:.2f}".format(desconto))
    print("O valor a ser pago com desconto é de R$ {0:.2f}".format(valor_liquido))
    print("O valor médio por passageiro é de R$ {0:.2f}".format(media_pax))

elif viajantes >= 4:
    if voo == "ECONÔMICA":
        desconto = valor_bruto * 0.05
        valor_liquido = valor_bruto - desconto
        media_pax = valor_liquido/viajantes
    elif voo == "EXECUTIVA":
        desconto = valor_bruto * 0.08
        valor_liquido = valor_bruto - desconto
        media_pax = valor_liquido / viajantes
    elif voo == "PRIMEIRA CLASSE":
        desconto = valor_bruto * 0.20
        valor_liquido = valor_bruto - desconto
        media_pax = valor_liquido / viajantes

    print("O valor bruto da viagem é R$ {0:.2f}".format(valor_bruto))
    print("O valor total do desconto é de R$ {0:.2f}".format(desconto))
    print("O valor a ser pago com desconto é de R$ {0:.2f}".format(valor_liquido))
    print("O valor médio por passageiro é de R$ {0:.2f}".format(media_pax))

else:
    print("Digite um valor válido!")