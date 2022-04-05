'''4) Uma companhia aérea define os preços de suas passagens a partir da
informação do destino bem como do número de passagens (se é apenas ida ou
se inclui também a volta). Faça um programa em Python que solicite o destino
bem como se o cliente deseja somente ida ou ida e volta. Informe o preço de
acordo com a tabela abaixo (PS: a empresa não trabalha nos trechos sul e
sudeste).
'''

print("************* BEM VINDE A AGÊNCIA DE VIAGENS PRIX PELO MUNDO! ****************")
regiao = input("Digite a região que deseja consultar: ").upper()
trecho = input("Informe se deseja comprar somente ida ou ida e volta: ").upper()

if regiao == "SUL" or regiao == "SUDESTE":
    print("Não operamos na região {} conforme desejado.".format(regiao))
elif regiao == "NORTE" and trecho == "IDA":
    print("O valor do trecho apenas de ida para a região {}, é de R$ 280,00".format(regiao))
elif regiao == "NORTE" and trecho == "IDA E VOLTA":
    print("O valor do trecho ida e volta para a região {}, é de R$ 400,00".format(regiao))
elif regiao == "NORDESTE" and trecho == "IDA":
    print("O valor do trecho apenas de ida para a região {}, é de R$ 380,00".format(regiao))
elif regiao == "NORDESTE" and trecho == "IDA E VOLTA":
    print("O valor do trecho ida e volta  para a região {}, é de R$ 628,00".format(regiao))
elif regiao == "CENTRO-OESTE" and trecho == "IDA":
    print("O valor do trecho apenas de ida para a região {}, é de R$ 620,00".format(regiao))
elif regiao == "CENTRO-OESTE" and trecho == "IDA E VOLTA":
    print("O valor do trecho ida e volta para a região {}, é de R$ 1.100,00".format(regiao))