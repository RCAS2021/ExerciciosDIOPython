#Tupla é imutável lista é mutável -> se criei uma tupla, até o final do programa ela é igual. Utilizar quando quer ter certeza que o valor não irá mudar
while True:
    selecionar = int(input("1- Criando Tuplas 2- Acessando Índice 3- Matriz 4- Fatiamento 5- For 6- Enumerate 7- Métodos\n"))

    if selecionar == 0:
        break

    if selecionar == 1:
        frutas = ("laranja", "pera", "uva",) #colocar uma vírgula no final para evitar erros de precedência
        letras = tuple("python")
        numeros = tuple([1, 2, 3, 4]) #passando uma lista para tupla, tornando os valores imodificáveis
        pais = ("brasil",)
        print(frutas)
        print(letras)
        print(numeros)
        print(pais)
    
    if selecionar == 2:
        frutas = ("maçã", "laranja", "uva",)
        print(frutas[0])
        print(frutas[2])
        print(frutas[-1])

#Matriz de tuplas
    if selecionar == 3:
        matriz = [ #tupla de tuplas
        [1,"a",2],
        ["b",3,4],
        [6,5,"c"], #lembrar de colocar a vírgula no final
        ]

        print(matriz[0]) #printa a primeira lista da matriz
        print(matriz[0][0]) #printa a primeira lista da matriz, no índice 0 da lista
        print(matriz[0][-1]) #printa a primeira lista da matriz, no índice -1 -> último elemento da lista
        print(matriz[-1][-1]) #printa a última lista da matriz, no índice -1 -> último elemento da lista
    
#Fatiamento de tuplas
    if selecionar == 4:
        lista = tuple("python") #ou lista = ["p","y","t","o","n"]
        print(lista[2:]) #printa do índice 2 até o fim
        print(lista[:2]) #printa do início até o índice 2
        print(lista[1:3]) #printa do índice 1 até o índice 3
        print(lista[0:3:2]) #printa do índice 0 até o índice 3, a cada 2(step)
        print(lista[::-1]) #printa do ínicio ao fim, iniciando pelo fim (espelha a string)
    
#Iterar utilizando for
    carros = ["Gol","Celta","Palio"]
    if selecionar == 5:

        for carro in carros:
            print(carro)

#Iterar utilizando Enumerate
    if selecionar == 6:
        for indice, carro in enumerate(carros):
            print(f"{indice}: {carro}")

#Métodos das tuplas
    if selecionar == 7:
        print("Count, Index e Len")