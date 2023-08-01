#FOR

selecionar = -1
VOGAIS = "AEIOU"
while selecionar != 0:
    selecionar = int(input("\n1- For 2- ForElse 3- Range 4- List Range 5- Range Normal 6- Range Step\n"))
    
    if selecionar == 1:
        texto = input("Informe um texto: ")
        for letra in texto:
            if letra.upper() in VOGAIS:
                print(letra, end="")
        print()

#FOR ELSE -- Não muito comum
    elif selecionar == 2:
        texto = input("Informe um texto: ")
        for letra in texto:
            if letra.upper() in VOGAIS:
                print(letra, end="")
        else:
            print() # adiciona uma quebra de linha
            print("Executa no final do laço")

#RANGE
    elif selecionar == 3:
        print(range(10)) #printa 0,10

    elif selecionar == 4:
        print(list(range(10))) #printa lista de 0 a 10

    elif selecionar == 5:
        for numero in range(11): #percorre normal
            print(numero, end=" ")

    elif selecionar == 6:
        for numero in range(0,52,5): #percorre a cada 5 números(step)
            print(numero, end=" ")