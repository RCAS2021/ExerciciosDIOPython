num_pedidos = int(input())

for i in range(1, num_pedidos + 1):
    prato = input()
    calorias = int(input())
    eh_vegano = input()
    if (eh_vegano == "s"):
        eh_vegano_bool = "Vegano"
    else:
        eh_vegano_bool = "Nao-vegano"
    print(f"Pedido {i}: {prato} ({eh_vegano_bool}) - {calorias} calorias")