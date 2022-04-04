valor_compra = float(input("Digite o valor total da compra: R$ "))
cupom = input("Digite um cupom de desconto válido: ").upper()

if cupom == "NIVER10":
    total_compra = valor_compra * 0.9
    print("O valor total da compra é de R$ {}".format(total_compra))
else:
    print("Cupom Inválido! \nTotal da compra R$ {}".format(valor_compra))

