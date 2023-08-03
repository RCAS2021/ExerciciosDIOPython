while True:
    frutas = ["laranja", "maçã", "uva", "pera"] #forma comum de lista
    selecionar = int(input("1- Listas 2- Matriz 3- Fatiamento de listas 4- For 5- Enumerate 6- Filtrar 7- Compreensão 8- Métodos\n"))
    
    if selecionar == 0:
        break

    if selecionar == 1:
        print(frutas)
        print(frutas[0]) #printa no índice 0
        print(frutas[2]) #printa no índice 2
        print(frutas[-1]) #printa no índice -1 -> último elemento da lista

        frutas = [] #lista vazia
        print(frutas)

        letras = list("python") #declarando com consultor list, cada letra é um elemento - argumento iteravel(string)
        print(letras)

        numeros = list(range(10)) #declara um elemento pra cada numero da range
        print(numeros)

        carro = ["Ferrari", "F8", 42000000, 2020, 2900, "São Paulo", True] #lista com diferentes atributos
        print(carro)

    if selecionar == 2:
        matriz = [ #lista de listas vira uma matriz 3x3
        [1,"a",2],
        ["b",3,4],
        [6,5,"c"]
        ]
        print(matriz[0]) #printa a primeira lista da matriz
        print(matriz[0][0]) #printa a primeira lista da matriz, no índice 0 da lista
        print(matriz[0][-1]) #printa a primeira lista da matriz, no índice -1 -> último elemento da lista
        print(matriz[-1][-1]) #printa a última lista da matriz, no índice -1 -> último elemento da lista

#Fatiamento de listas

    if selecionar == 3:
        lista = list("python") #ou lista = ["p","y","t","o","n"]
        print(lista[2:]) #printa do índice 2 até o fim
        print(lista[:2]) #printa do início até o índice 2
        print(lista[1:3]) #printa do índice 1 até o índice 3
        print(lista[0:3:2]) #printa do índice 0 até o índice 3, a cada 2(step)
        print(lista[::-1]) #printa do ínicio ao fim, iniciando pelo fim (espelha a string)

#Iterar utilizando for
    carros = ["Gol","Celta","Palio"]
    if selecionar == 4:

        for carro in carros:
            print(carro)

#Iterar utilizando Enumerate
    if selecionar == 5:
        for indice, carro in enumerate(carros):
            print(f"{indice}: {carro}")

#Filtrando através de listas, criando uma lista nova
    
    if selecionar == 6:
        numeros = [1, 30, 21, 2, 9, 65, 34]
        pares = []
        for numero in numeros:
            if numero % 2 == 0:
                pares.append(numero) #forma de adicionar novos valores à lista
        print(pares)

#Comprehension (Compreensão de listas)
    if selecionar == 7:
        numeros = [1, 30, 21, 2, 9, 65, 34]
        pares = [numero for numero in numeros if numero % 2 == 0] #coloca o for e if em uma linha -> 1 parte é o retorno(numero), 2 parte a iteração (for...) 3 parte a condição(if...)
        quadrado = [numero ** 2 for numero in numeros]
        print(pares)
        print(quadrado)

    if selecionar == 8:
        print("Append, Clear, Copy, Count, Extend, index, Pop, Remove, Reverse, Sort, Sorted")