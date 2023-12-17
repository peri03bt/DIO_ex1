menu = """
[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Sair
"""
saldo = 0
numero_de_saques = 0
extrato = ''

LIMITE_SAQUE = 500
QTIDADE_MAX_SAQUE = 3


while True:
    print(menu)
    opcao = input("Digite aqui sua opção: ").strip()
    print()
    if opcao == "1":#DEPÓSITO
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito -> R$ {valor:,.2f}\n'
            print(f'Depósito realizado com sucesso!\nObrigado por usar nosso Banco.\nSaldo:R$ {saldo:,.2f}')
        else:
            print("Valor de depósito negativo!")

    elif opcao == "2":#SAQUE
        valor = float(input("\nDigite o valor para saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > LIMITE_SAQUE

        excedeu_saque = numero_de_saques >= QTIDADE_MAX_SAQUE

        if excedeu_saldo:
            print(f'Saldo insuficiente!\nSaldo: R$ {saldo:,.2f}')
        elif excedeu_limite:
            print(f'Limite de R$ {LIMITE_SAQUE:,.2f} excedido')
        elif excedeu_saque:           
            print(f'Limite de atingido de {QTIDADE_MAX_SAQUE} diário.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque -> R$ -{valor:,.2f}\n'
            numero_de_saques += 1
            print(f'Saque realizado com sucesso!\nObrigado por usar nosso Banco.\nSaldo:{saldo:,.2f}')

    elif opcao == "3":#EXTRATO
        print(" extrato ".upper().center(40,'#'))
        print()
        print("Não realizado movimentações nessa conta" if not extrato else extrato)
        print('_'*40)
        print(f"Saldo: R$ {saldo:,.2f}")
        print('_'*40)
    elif opcao == "4":#SAIR
        break
