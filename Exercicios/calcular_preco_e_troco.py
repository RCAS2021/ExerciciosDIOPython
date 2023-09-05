valor_hamburguer = float(input())
quantidade_hamburguer = int(input())
valor_bebida = float(input())
quantidade_bebida = int(input())
valor_pago = float(input())


total_hamburgueres = (valor_hamburguer * quantidade_hamburguer)
total_bebidas = (valor_bebida * quantidade_bebida)
preco_final = total_hamburgueres + total_bebidas
troco = valor_pago - preco_final

print(f"O preço final do pedido é R$ {preco_final:.2f}. Seu troco é R$ {troco:.2f}.")