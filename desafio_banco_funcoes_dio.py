def sacar(*, saque, extrato, saldo, numero_saques, limite_numero_saques, limite_saque):
    saque = float(input(f"\nSaldo disponível:R${saldo:.2f}\nDigite o valor a ser sacado: "))
    if saque > saldo:
        print("\nSaldo insuficiente.")
    elif saque > limite_saque:
        print("\nSaque excedeu o limite.")
    elif numero_saques >= limite_numero_saques:
        print("\nNumero de saques atingido.")
    elif saque <= 0:
        print("Valor inválido")
    else:
        saldo -= saque
        print(f"\nSaque efetuado, novo saldo:R${saldo:.2f}")
        extrato.append(f"Saque    -R${saque:.2f}")
        numero_saques +=1
    return saldo, extrato, numero_saques

def depositar(saldo, extrato, /):
    deposito = float(input("\nDigite a quantidade a depositar: "))
    if deposito < 0:
        print("\nValor inválido")
    else:
        saldo += deposito
        print(f"\nDepósito efetuado com sucesso! Novo saldo:R${saldo:.2f}")
        extrato.append(f"Depósito +R${deposito:.2f}")
    return extrato, saldo

def exibe_extrato(saldo, /, *, extrato):
    print("Extrato:")
    for i in extrato:
        print(i)
    print(f"Saldo:   R${saldo:.2f}")

def criar_usuario(usuarios):

    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já existente")
        return
    
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento")
    endereco = input("Digite o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
            
    if usuario:
        print("Conta do banco criada!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        
    print("Conta de usuário não encontrada!")

def listar_contas(contas):
    for conta in contas:
        linha = f"Agência: {conta['agencia']}, Número da conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}"
        print(linha)

def menu():
    menu = """
            ===========MENU==========
            1- Criar usuário
            2- Criar conta do banco
            3- Depositar
            4- Sacar
            5- Extrato
            0- Sair
            =========================
            """
    return menu

saldo = 0
LIMITE_SAQUE = 500
numero_saques = 0
LIMITE_NUMERO_SAQUES = 3
AGENCIA = "0001"
extrato = []
usuarios = []
contas = []
numero_conta = 1


while True:
    selecionar = int(input(menu()))

    if selecionar == 1:
        criar_usuario(usuarios)
    
    elif selecionar == 2:
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
        numero_conta += 1
    
    elif selecionar == 6:
        listar_contas(contas)

    elif selecionar == 3:
        extrato, saldo = depositar(saldo, extrato)
    
    elif selecionar == 4:
        saldo, extrato, numero_saques = sacar(limite_saque = LIMITE_SAQUE, limite_numero_saques = LIMITE_NUMERO_SAQUES, extrato = extrato, saldo = saldo, numero_saques = numero_saques)
    
    elif selecionar == 5:
        exibe_extrato(saldo, extrato = extrato)
    
    elif selecionar == 0:
        break
    
    else:
        print("\nOpção não existente")