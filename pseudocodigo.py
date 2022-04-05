num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

resultado = ((num1%2)*3)+(13-2+num2)
print(resultado)
if resultado <=0:
    print("Resultado menor ou igual a zero.")
elif resultado > 0 and resultado <=20:
    print("Resultado maior que zero e menor ou igual a 20.")
else:
    print("Resultado maior que 20.")

