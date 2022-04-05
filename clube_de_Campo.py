'''6) Escreva um programa em Python que receba informações de 1 (um) dia de
atendimento de um recepcionista:
O usuário digitará:
- Nome do recepcionista
- Quantidade de pessoas que frequentou cada atividade. É necessário digitar a
quantidade para cada atividade.
Calcule e mostre na tela o seguinte relatório referente ao atendimento do
recepcionista:
Prezado(a) ______________,
Na data de hoje, _______________ pessoas frequentaram o Clube de Campo
Viver a vida com alegria.
____ % da atividade YOGA
____ % da atividade NATAÇÃO
____ % da atividade HIDROGINÁSTICA
____ % da atividade GINÁSTICA ARTÍSTICA
A atividade com maior participação foi:
'''

print("********** Bem vindo ao Clube de Campo Viver a Vida com Alegria! **********")
recep = input("Digite o nome do recepcionista do dia: ")
yoga = int(input("Informe o total de pessoas que participaram da aula de Yoga no dia de hoje: "))
natacao = int(input("Informe o total de pessoas que participaram da aula de Natação no dia de hoje: "))
hidro = int(input("Informe o total de pessoas que participaram da aula de Hidroginástica no dia de hoje: "))
gin_art = int(input("Informe o total de pessoas que participaram da aula de Ginástica Artística no dia de hoje: "))

total_pessoas = yoga + natacao + hidro + gin_art
porc_yoga = (100*yoga)/total_pessoas
porc_nat = (100*natacao)/total_pessoas
porc_hidro = (100*hidro)/total_pessoas
porc_gin = (100*gin_art)/total_pessoas

print("Prezado(a) {}, \n\nNa data de hoje, {} pessoas frequentaram o Clube de Campo Viver a vida com alegria. \n{:.0f}% da atividade YOGA \n{:.0f}% da atividade NATAÇÃO\n{:.0f}% da atividade HIDROGINÁSTICA\n{:.0f}% da atividade GINÁSTICA ARTÍSTICA\n".format(recep,total_pessoas,porc_yoga,porc_nat, porc_hidro, porc_gin))

if total_pessoas <=50:
    print("Hoje o movimento do clube foi baixo.")
elif total_pessoas >50 and total_pessoas<=150:
    print("Hoje o movimento do clube foi normal.")
else:
    print("Hoje o movimento do clube foi excelente, acima da média.")

if porc_yoga>porc_gin and porc_yoga>porc_nat and porc_yoga>porc_hidro:
    print("A atividade com maior participação foi o Yoga.")
elif porc_hidro>porc_gin and porc_hidro>porc_nat and porc_hidro>porc_yoga:
    print("A atividade com maior participação foi a Hidroginástica.")
elif porc_nat>porc_gin and porc_nat>porc_yoga and porc_nat>porc_hidro:
    print("A atividade com maior participação foi a Natação.")
elif porc_gin>porc_nat and porc_gin>porc_yoga and porc_gin>porc_hidro:
    print("A atividade com maior participação foi a Ginástica Artística.")
else:
    print("Hoje as aulas foram um sucesso!!")
