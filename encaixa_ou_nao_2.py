qt = int(input())

v = []



for i in range(qt):

  v = input().split(" ")

  a = v[0]

  b = v[1]



  if len(b) > len(a):

    print("nao encaixa")

  elif a.endswith(b):

    print("encaixa")

  else:

    print("nao encaixa")
