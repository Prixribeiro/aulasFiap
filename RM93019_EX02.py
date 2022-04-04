'''2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives. Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.'''

segunda= int(input("Digite quantos alunos preferem as lives as SEGUNDAS-FEIRA: "))
terca= int(input("Digite quantos alunos preferem as lives as TERÇAS-FEIRA: "))
quarta= int(input("Digite quantos alunos preferem as lives as QUARTAS-FEIRA: "))
quinta= int(input("Digite quantos alunos preferem as lives as QUINTAS-FEIRA: "))
sexta= int(input("Digite quantos alunos preferem as lives as SEXTAS-FEIRA: "))


if segunda > terca and segunda > quarta and segunda >quinta and segunda>sexta:
    print("O dia escolhido pela maioria dos alunos foi: SEGUNDA-FEIRA, com {} votos.".format(segunda))
elif terca>segunda and terca>quarta and terca>quinta and terca>sexta:
    print("O dia escolhido pela maioria dos alunos foi: TERÇA-FEIRA, com {} votos.".format(terca))
elif quarta>segunda and quarta>terca and quarta>quinta and quarta>sexta:
    print("O dia escolhido pela maioria dos alunos foi: QUARTA-FEIRA, com {} votos.".format(quarta))
elif quinta>segunda and quinta>terca and quinta>quarta and quinta>sexta:
    print("O dia escolhido pela maioria dos alunos foi: QUINTA-FEIRA, com {} votos.".format(quinta))
elif sexta>segunda and sexta>terca and sexta>quarta and sexta>quinta:
    print("O dia escolhido pela maioria dos alunos foi: SEXTA-FEIRA, com {} votos.".format(sexta))
else:
    print("Houve empate, todos votam novamente!")