#criação de uma tupla
categorias=("padawan","knight","master")
print(categorias)
#exibindo um item específico da tupla
print(categorias[1])

#para desempacotar uma tupla
#cada item da tupla vira uma variável
teste1,teste2,teste3 = categorias
print(teste1)
print(teste2)
print(teste3)

#para navegar pela tupla com um looping for
for categoria in categorias:
    print(categoria)

