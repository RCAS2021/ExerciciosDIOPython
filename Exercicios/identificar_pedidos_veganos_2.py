##Versão DIO com if ternário

num_pedidos = int(input())

for i in range(1, num_pedidos + 1):
    prato = input()
    calorias = int(input())
    eh_vegano = input()
    eh_vegano_bool = "Vegano" if eh_vegano == "s" else "Nao-vegano"
    print(f"Pedido {i}: {prato} ({eh_vegano_bool}) - {calorias} calorias")