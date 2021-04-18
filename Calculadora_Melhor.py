print("Bem vindo ao meu projeto de calculadora v0.2 -By KriegerThiago")
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

print("Digite 1 - Subtração / 2 - Divisão / 3 - Multiplicação / 4 - Soma : ")
funcao = input()


if funcao == str(1):
    resultado = float(num1) - float(num2)
    print("O resultado da SUBTRAÇÃO dos números é: " + format(resultado,".2f"))
elif funcao == str(2):
    resultado = float(num1) / float(num2)
    print("O resultado da DIVISÃO dos números é: " + format(resultado,".2f"))
elif funcao == str(3):
    resultado = float(num1) * float(num2)
    print("O resultado da  MULTIPLICAÇÃO dos números é: " + format(resultado,".2f"))
elif funcao == str(4):
    resultado = float(num1) + float(num2)
    print("O resultado da SOMA dos números é: " + format(resultado,".2f"))
else:
    print("Erro, coloque o número da devida função e tente novamente.")
