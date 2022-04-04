'''Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria: um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.

Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês.'''

print("**** Bem vindo ao estúdio de Produção Multimídia da FIAP ****")
assinatura = input("Por favor, informe qual é sua assinatura: Basic, Silver, Gold ou Platinum: ").upper()
faturamento = float(input("Por favor, digite o valor do faturamento anual do seu canal: R$ "))

if assinatura == "BASIC":
    bonus = faturamento * 0.30
    print("Devido sua assinatura atual ser a {}, o valor do bônus anual a ser pago é de R$ {:.2f}".format(assinatura,bonus))
elif assinatura == "SILVER":
    bonus = faturamento * 0.20
    print("Devido sua assinatura atual ser a {}, o valor do bônus anual a ser pago é de R$ {:.2f}".format(assinatura,bonus))
elif assinatura == "GOLD":
    bonus = faturamento * 0.10
    print("Devido sua assinatura atual ser a {}, o valor do bônus anual a ser pago é de R$ {:.2f}".format(assinatura,bonus))
elif assinatura == "PLATINUM":
    bonus = faturamento * 0.05
    print("Devido sua assinatura atual ser a {}, o valor do bônus anual a ser pago é de R$ {:.2f}".format(assinatura, bonus))
else:
    print("Digite uma assinatura válida!")