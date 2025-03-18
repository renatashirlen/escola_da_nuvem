# Programa que calcule o valor da gorjeta baseado no valor total da conta através de uma porcentagem pré estabelecida


def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)


total_conta = float(input("Digite o valor da sua conta: "))
porcentagem = 15
gorjeta = calcular_gorjeta(total_conta, porcentagem)

print(
    f"O valor da conta é de R${total_conta:.2f}, a gorjeta de {porcentagem}% é de R${gorjeta:.2f} "
)
