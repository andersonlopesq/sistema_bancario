print("\nSeja bem-vindo! \nSelecione a operação desejada.")

menu = """
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Valor do depósito: "))

        if valor > 0:
            saldo += valor 
            extrato += f"Depósito ------- (+)R$ {valor:.2f}\n"
        
        else:
            print("O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Valor do saque: "))

        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saque_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("Não há saldo disponível para esta operação. Consulte seu extrato.")
        
        elif limite_excedido:
            print("O valor máximo por saque é de R$ 500,00.")

        elif saque_excedido:
            print("Você já atingiu o limite de 03 saques diários.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque ---------- (-)R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            "O valor informado é inválido."

    elif opcao == "e":
        print("\n~~~~~~~~~~ EXTRATO ~~~~~~~~~~")
        print("Você ainda não realizou nenhuma operação." if not extrato else extrato)
        print(f"Saldo ------------- R$ {saldo:.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    elif opcao == "q":
        break

    else:
        print("Operação inválida. Selecione novamente a operação desejada.")
