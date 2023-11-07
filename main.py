conta_saldo = 0
saque = 0
extrato = " "
limite_quantidade_saque = 3
limite_valor = 500

while True:
    operacao = input("Qual operação você deseja fazer? \n"
                     "[1] Depósito\n"
                     "[2] Saque \n"
                     "[3] Extrato \n"
                     "[4] Sair \n")
    if operacao == "1":
        valor_deposito = float(input("Digite o valor que você deseja depositar: \n"))
        conta_saldo += valor_deposito
        extrato += f"-Foi depositado:           + R${valor_deposito:5.2f} \n"
    if operacao == "2":
        if limite_quantidade_saque == 0:
            print(f"Limite de saque excedido. \n")
        else:
            valor_saque = float(input("Digite o valor que você deseja sacar: \n"))
            if valor_saque > limite_valor:
               print(f"Valor por saque excedido! \n")
            elif conta_saldo < valor_saque:
                print("Não foi possível efetuar o saque por falta de saldo!")
            else:
                conta_saldo -= valor_saque
                limite_quantidade_saque -= 1
                extrato += f"-Foi sacado:               - R${valor_saque:5.2f}\n"

    if operacao == "3":
        print("\n====================================================")
        print(extrato)
        print(f"O seu saldo atual é de R${conta_saldo:5.2f}")
        print("====================================================\n")

    if operacao == "4":
        break



