import datetime

contador_saques = 0
data_ultimo_saque = datetime.date.today()

def adicionar_transacao(extrato, tipo, valor, saldo):
    transacao = f"{tipo}: R${valor:.2f} | Saldo atual: R${saldo:.2f}"
    extrato.append(transacao)


def depositar(saldo, extrato):
    try:
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        print(f"Depósito realizado com sucesso! Novo saldo: R${saldo:.2f}")
        adicionar_transacao(extrato, "Depósito", valor, saldo)
        return saldo
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")
        return saldo


def sacar(saldo, extrato, contador_saques, data_ultimo_saque):
    try:
        hoje = datetime.date.today()
        if data_ultimo_saque != hoje:
            contador_saques = 0
            data_ultimo_saque = hoje

        if contador_saques >= 3:
            print("Limite de saques diários atingido.")
            return saldo, contador_saques, data_ultimo_saque

        valor = float(input("Digite o valor do saque: "))

        if valor <= 0:
            print("O valor do saque deve ser positivo.")
            return saldo, contador_saques, data_ultimo_saque

        if valor > saldo:
            print("Saldo insuficiente para o saque.")
            return saldo, contador_saques, data_ultimo_saque

        if valor > 500:
            print("O valor máximo para saque é R$500.")
            return saldo, contador_saques, data_ultimo_saque

        saldo -= valor
        print(f"Saque realizado com sucesso! Novo saldo: R${saldo:.2f}")
        adicionar_transacao(extrato, "Saque", valor, saldo)

        contador_saques += 1
        return saldo, contador_saques, data_ultimo_saque

    except ValueError:
        print("Valor inválido. Por favor, digite um número.")
        return saldo, contador_saques, data_ultimo_saque

def mostrar_extrato(extrato):
    print("Extrato:")
    if not extrato:
        print("Nenhuma transação realizada.")
    for transacao in extrato:
        print(transacao)

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        saldo = depositar(saldo, extrato)

    elif opcao == "2":
        print("Saque")
        saldo, contador_saques, data_ultimo_saque = sacar(saldo, extrato, contador_saques, data_ultimo_saque)

    elif opcao == "3":
        mostrar_extrato(extrato)

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")