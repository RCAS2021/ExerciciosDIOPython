while True:
    selecionar = int(input("1- Append 2- Clear 3- Copy 4- Count 5- Extend 6- index 7- Pop 8- Remove 9- Reverse 10- Sort 11- Sorted\n"))

    if selecionar == 1: #append -> coloca no último índice da lista
        lista = []
        lista.append(1)
        lista.append("Python")
        lista.append([40,30,20])
        print(lista)

    if selecionar == 2:
        lista = [1, "Python", [40,30,20]]
        print(lista)
        lista.clear()
        print(lista)

    if selecionar == 3:
        lista [1, "Python", [40,30,20]]
        l2 = lista.copy()
        print(lista)
        print(l2)
        print(id(l2), id(lista)) #para comprovar que as listas são diferentes
        l2[0] = 2 #quando altera a l2, não altera a lista
    
    if selecionar == 4:
        cores = ["Vermelho", "Azul", "verde", "azul", "Azul"] #Case sensitive
        print(cores.count("Vermelho"))
        print(cores.count("azul"))
        print(cores.count("Azul"))
        print(cores.count("verde"))

    if selecionar == 5:
        linguagens = ["Python", "JS", "C"]
        print(linguagens)
        linguagens.extend(["JAVA", "C#"]) #passa uma outra lista, não elimina os valores duplicados
        print(linguagens)
    
    if selecionar == 6:
        linguagens = ["Python", "JS", "C", "JAVA"] #passa a primeira ocorrência (se tiver mais de uma ocorrência, passa apenas a primeira)
        print(linguagens.index("JAVA"))
        print(linguagens.index("Python"))

    if selecionar == 7:
        linguagens = ["Python", "JS", "C", "JAVA"] #listas funcionam como pilhas, o pop tira o último elemento da lista
        linguagens.pop()
        linguagens.pop()
        linguagens.pop(0)
        print(linguagens)
    
    if selecionar == 8:
        linguagens = ["Python", "JS", "C", "JAVA"] #parecido com o pop, remove o que foi indicado no parâmetro da lista, remove apenas a primeira ocorrência
        linguagens.remove("C")
        print(linguagens)
    
    if selecionar == 9:
        linguagens = ["Python", "JS", "C", "JAVA"] #inverte a lista
        linguagens.reverse()
        print(linguagens)
    
    if selecionar == 10:
        linguagens = ["Python", "JS", "C", "JAVA"]
        linguagens.sort() #ordena por ordem alfabética
        linguagens.sort(reverse = True) #ordena por ordem alfabética inversa (reverse=True)
        linguagens.sort(key=lambda x: len(x)) #ordena pelo tamanho (x: len(x)) -> key=lambda é uma função anônima(?)
        linguagens.sort(key=lambda x: len(x), reverse=True) #ordena pelo tamanho inverso (x: len(x), reverse=True)
    
    if selecionar == 11:
        linguagens = ["Python", "JS", "C", "JAVA"]
        sorted(linguagens, key=lambda x: len(x))
