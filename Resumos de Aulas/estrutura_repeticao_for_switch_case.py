#FOR

selecionar = input("1- For 2- ForElse 3- Range 4- List Range 5- Range Normal 6- Range Step\n")
VOGAIS = "AEIOU"
match selecionar:
    case "1":
        texto = input("Informe um texto: ")
        for letra in texto:
            if letra.upper() in VOGAIS:
                print(letra, end="")
        print()

#FOR ELSE -- Não muito comum
    case "2":
        texto = input("Informe um texto: ")
        for letra in texto:
            if letra.upper() in VOGAIS:
                print(letra, end="")
        else:
            print() # adiciona uma quebra de linha
            print("Executa no final do laço")

#RANGE
    case "3":
        print(range(10)) #printa 0,10

    case "4":
        print(list(range(10))) #printa lista de 0 a 10

    case "5":
        for numero in range(11): #percorre normal
            print(numero, end=" ")

    case "6":
        for numero in range(0,52,5): #percorre a cada 5 números(step)
            print(numero, end=" ")