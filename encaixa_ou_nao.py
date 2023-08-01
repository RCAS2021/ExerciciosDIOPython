#Versão minha - verificar se encaixa uma variável dentro de outra
qt = int(input())

v = []



for i in range(qt):

  v = input().split(" ") #para escrever os dois números em uma linha

  a = v[0]

  b = v[1]

  if a in b or b in a:
    print("encaixa")
    
  else:
    print("nao encaixa")