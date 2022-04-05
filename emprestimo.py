'''3) A prefeitura de Recife criou um programa de empréstimo para seus funcionários
com desconto em folha. O valor da prestação não pode ultrapassar 30% do salário
bruto do funcionário. Faça um programa em Python que solicite o valor do salário
bruto, o valor da prestação e informe se o empréstimo pode ou não ser concedido.
Validações:
Não aceitar salário <=0
Não aceitar prestação <=0'''

salario = float(input("Digite o valor do seu salário atual: R$ "))
prestacao = float(input("Digite o valor da prestação: R$ "))

limite = salario * 0.30

if salario <=0:
    print("Digite um valor de salário válido!")
elif prestacao<=0:
    print("Digite um valor de prestação válido.")
elif prestacao > limite:
    print("Infelizmente, o empréstimo não pode ser concedido, pois a prestação ultrapassa o valor de 30% do seu salário.")
elif prestacao <= limite:
    print("Parabéns! O empréstimo será concedido.")

