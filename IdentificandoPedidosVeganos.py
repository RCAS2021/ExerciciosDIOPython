numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input()
    if (ehVegano == "s"):
        ehVeganoBool = "Vegano"
    else:
        ehVeganoBool = "Nao-vegano"
    print(f"Pedido {i}: {prato} ({ehVeganoBool}) - {calorias} calorias")