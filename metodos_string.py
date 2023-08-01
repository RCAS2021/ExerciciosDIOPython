while True:
    selecionar = int(input("\n1- UpperLowerTitle 2- Strip 3- CenterJoin 4- FatiamentoString 5- Múltiplas Linhas\n"))

    if selecionar == 0:
        break

    elif selecionar == 1:
        nome = "PuDha"
        print(nome.upper())
        print(nome.lower())
        print(nome.title())

    elif selecionar == 2:
        nome = "  PuDha   "
        print(nome.strip())
        print(nome.lstrip())
        print(nome.rstrip())
        print(nome.strip() + ".")

    elif selecionar == 3:
        nome = "Pudha"
        print(nome.center(11, "*"))
        print("-".join(nome))
    
    elif selecionar == 4:
        nome = "Pudha Cruz"
        print(nome[3]) #Pega o 3 caracter
        print(nome[:8]) #Pega até o 8 caracter
        print(nome[6:]) #Pega depois do 6 caracter
        print(nome[6:9]) #Pega entre o 6 e 9 caracter
        print(nome[0:9:3]) #Pega entre o primeiro e 9 caracter, de 3 em 3 (step)
        print(nome[:]) #pega do inicio ao fim
        print(nome[::-1]) #espelha a string [9:-1:-1] (inicio:fim:step)
        print(nome[9:-1:-1]) #exemplo anterior
    
    elif selecionar == 5:
        print(
        """
        ===========MENU==========
        1- UpperLowerTitle
        2- Strip
        3- CenterJoin
        4- FatiamentoStrings
        5- MultiplasLinhas
        """
        )
        
