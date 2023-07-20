def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor

    desconto = input()
    if(desconto == "10%"):
        total -= (total*0.1)
    else:
        total -= (total*0.2)
    print(f"Valor total: {total:.2f}")

if __name__ == "__main__":
    main()