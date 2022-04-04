#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

#incluindo um valor no final da lista
jedi.append("Lia Clark")

#incluindo um valor no final da lista com o usuário digitando
jedi.append(input("Digite o nome de um Jedi: "))

#incluindo um valor na lista com indice específico
jedi.insert(2, "Priscila")

#pedindo ao usuário o nome para incluir em posição específica
jedi.insert(4,input("Digite outro nome Jedi: "))

#Removendo o último item da lista
jedi.pop()

#removendo um item em posicção específica
jedi.pop(1)

#removendo um valor específico independente da posição
jedi.remove("Obi-Wan")

#A variável assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)