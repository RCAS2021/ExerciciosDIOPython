while True: #conjuntos é a estrutura de dados set que não possui objetos repetidos - elimina os objetos duplicados - não garante a ordem - não suportam indexação e fatiamento
    selecionar = int(input("1- Exemplo Duplicados 2- Indexação 3- Métodos\n"))

    if selecionar == 0:
        break

    if selecionar == 1:
        print(set([1, 2, 3, 1, 3, 4]))
        print(set("abacaxi"))
        print(set(("palio", "gol", "celta", "palio")))
        print({"a","a","b","c","b"}) #Exemplo outro modo de utilizar set, utilizando {}
    
    if selecionar == 2:
        numeros = {1, 2, 3, 2}
        numeros = list(numeros) #precisa converter o conjunto para lista -> 'set' object is not subscriptable(não podem ser acessados)
        print(numeros[2])

        #Iterar dentro do for
        carros = {"gol", "celta", "palio"}
        for carro in carros:
            print(carro)

        #Iterar utilizando enumerate
        carros = {"gol", "celta", "palio"}
        for indice, carro in enumerate(carros):
            print(f"{indice}:{carro}")

#Métodos da classe set
    if selecionar == 3:
        while True:
            selecionar2 = int(input("1- Union 2- Intersection 3- Difference 4- Symmetric_difference 5- Issubset 6- Issuperset 7- Isdisjoint 8- Add 9- Clear 10- Copy 11- Discard 12- Pop 13- Remove 14- Len\n"))

            if selecionar == 0:
                break
#Union
            if selecionar == 1:
                print("union")
                conjunto_a = {1, 2, 3}
                conjunto_b = {3, 4, 5}
                print(conjunto_a)
                print(conjunto_b)
                print(conjunto_a.union(conjunto_b))

#Intersection
            if selecionar == 2:
                print("\nintersection")
                print(conjunto_a)
                print(conjunto_b)
                print(conjunto_a.intersection(conjunto_b))

#Difference
            if selecionar == 3:
                print("\ndifference")
                print(conjunto_a)
                print(conjunto_b)
                print(conjunto_a.difference(conjunto_b))
                print(conjunto_b.difference(conjunto_a))

#Symmetric_Difference
            if selecionar == 4:
                print("\nsymmetric_difference")
                print(conjunto_a)
                print(conjunto_b)
                print(conjunto_a.symmetric_difference(conjunto_b))

#issubset -> está contido
            if selecionar == 5:
                print("\nissubset")
                conjunto_a = {1, 2, 3}
                conjunto_b = {4, 1, 2, 5, 6, 3}
                print(conjunto_a)
                print(conjunto_b)
                print(conjunto_a.issubset(conjunto_b))
                print(conjunto_b.issubset(conjunto_a))

#issuperset -> contém
            if selecionar == 6:
                print("\nissuperset")
                conjunto_a = {1, 2, 3}
                conjunto_b = {4, 1, 2, 5, 6, 3}
                print(conjunto_a)
                print(conjunto_b)
                print(conjunto_a.issuperset(conjunto_b))
                print(conjunto_b.issuperset(conjunto_a))
    
#isdisjoint -> onde não tem uma interseção
            if selecionar == 7:
                print("\nisdisjoint")
                conjunto_a = {1, 2, 3, 4, 5}
                conjunto_b = {6, 7, 8, 9}
                conjunto_c = {1, 0}
                print(conjunto_a)
                print(conjunto_b)
                print(conjunto_c)
                print(conjunto_a.isdisjoint(conjunto_b))
                print(conjunto_a.isdisjoint(conjunto_c))

#add
            if selecionar == 8:
                print("\nadd")
                sorteio = {1, 23}
                print(sorteio)
                sorteio.add(25)
                sorteio.add(42)
                sorteio.add(25)
                print(sorteio)

#clear
            if selecionar == 9:
                print("\nclear")
                print(sorteio)
                sorteio.clear()
                print(sorteio)

#copy
            if selecionar == 10:
                print("\ncopy")
                sorteio = {1, 23}
                print(sorteio)
                sorteio2 = sorteio.copy()
                print(sorteio2)

#discard
            if selecionar == 11:
                print("\ndiscard")
                numeros = {1, 2, 3, 1, 2, 4, 5, 5}
                print(numeros)
                numeros.discard(1)
                numeros.discard(45) #não gera erro se descartar algo que não existe
                print(numeros)

#pop
            if selecionar == 12:
                print("\npop")
                print(numeros)
                print(numeros.pop()) #faz o pop do valor da frente
                print(numeros)

#remove
            if selecionar == 13:
                print("\nremove")
                print(numeros)
                numeros.remove(5)
                print(numeros)

#len
            if selecionar == 14:
                print("\nlen")
                numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
                print(1 in numeros)
                print(10 in numeros)