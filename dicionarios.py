while True: #conjunto não-ordenado de pares de chave:valor, onde as chaves são únicas. chave é um objeto imutável(tuplas), valor pode ser imutável ou mutável e qualquer tipo
    selecionar = int(input("1- Exemplo 2- Acesso 3- Dicionário aninhado 4- Métodos\n"))

    if selecionar == 0:
        break

    if selecionar == 1:
        pessoa = {"nome": "Pudha", "idade": 28} #método 1 -> nome=chave, guilherme=valor
        print(pessoa)
        pessoa = dict(nome="Pudha", idade = 28) #método 2 -> nome=chave, guilherme=valor
        print(pessoa)
        pessoa["telefone"] = "3333-1234" #adicionando nova chave e valor
        print(pessoa)
    
    if selecionar == 2:
        pessoa = {"nome": "Pudha", "idade": 28} #método 1 -> nome=chave, guilherme=valor
        print(pessoa)
        print(pessoa["nome"])
        print(pessoa["idade"])
        pessoa["nome"]="Lemin"
        pessoa["idade"]=26
        pessoa["telefone"]="0090-2234"
        print(pessoa)

    if selecionar == 3:
        contatos = {
            "aaaaa@hotmail.com": {"nome":"pudha", "telefone":"1234-4321"},
            "bbbbbb@gmail.com": {"nome":"pudhim", "telefone":"4312-5223"}
        }
        print(contatos)
        print(contatos["aaaaa@hotmail.com"])
        print(contatos["aaaaa@hotmail.com"]["telefone"])

#Iterar com for:
        for chave in contatos:
            print(chave, contatos[chave]) #não é a melhor a ser feita

        for chave, valor in contatos.items(): #método items retorna uma lista de tuplas, primeiro argumento é uma chave e o segundo um valor
            print(chave, valor)

#Métodos da classe dict
    if selecionar == 4:
        while True:
            selecionar2 = int(input("1- Clear 2- Copy 3- Fromkeys 4- Get 5- Items 6- Keys 7- Pop 8- Popitem 9- Setdefault 10- Update 11- Values 12- In 13- Del\n"))
            contatos = {
            "aaaaa@hotmail.com": {"nome":"pudha", "telefone":"1234-4321"},
            "bbbbbb@gmail.com": {"nome":"pudhim", "telefone":"4312-5223"}
            }
            if selecionar2 == 0:
                break
#Clear
            if selecionar2 == 1:
                print("clear")
                print(contatos)
                contatos.clear()
                print(contatos)

#Copy
            if selecionar2 == 2:
                print("\ncopy")
                print(contatos)
                contatos2 = contatos.copy()
                contatos2["aaaaa@hotmail.com"] = {"nome:" "TESTE"}
                print(contatos)
                print(contatos2)
                
#fromkeys
            if selecionar2 == 3:
                print("\nfromkeys") #cria chaves -> dict(nome_do_dicionario).fromkeys([chave], valor)
                dict.fromkeys(["nome", "telefone"]) #chaves sem valor
                dict.fromkeys(["nome", "telefone"], "vazio") #valores viram "vazio", cria um conjunto de chaves com um valor padrão

#get
            if selecionar2 == 4:
                print("\nget") #acessar valores
                print(contatos)
                #print(contatos["chave"]) #simulando erro, se a chave não existir, gera uma exceção
                print(contatos.get("chave")) #se não tem certeza se uma chave existe ou não, utiliza o método get
                print(contatos.get("chave", {})) #se não encontrar a chave, devolve um valor informado ({})
                print(contatos.get("aaaaa@hotmail.com", {}))

#items
            if selecionar2 == 5:
                print("\nitems")
                print(contatos.items()) #método items retorna uma lista de tuplas, primeiro argumento é uma chave e o segundo um valor

#keys
            if selecionar2 == 6:
                print("\nkeys")
                print(contatos.keys()) #retorna as chaves
    
#pop
            if selecionar2 == 7:
                print("\npop")
                print(contatos)
                contatos.pop("aaaaa@hotmail.com", {})
                print(contatos)

#popitem
            if selecionar2 == 8:
                print("\npopitem")
                print(contatos)
                contatos.popitem()
                print(contatos)

            contatos = {"nome" : "Pudha", "telefone": "1234-4321"}

#setdefault
            if selecionar2 == 9:
                print("\nsetdefault") #se o valor não existir no dicionário, adiciona, se já existir, retorna o que existe
                print(contatos)
                contatos.setdefault("nome", "Lemin")
                print(contatos)
                contatos.setdefault("idade", 28)
                print(contatos)

            contatos = {
            "aaaaa@hotmail.com": {"nome":"pudha", "telefone":"1234-4321"},
            "bbbbbb@gmail.com": {"nome":"pudhim", "telefone":"4312-5223"},
            "pudha@gmail.com": {"nome":"pudho", "telefone":"4421-5523"}
            }
            
#update
            if selecionar2 == 10:
                print("\nupdate") 
                contatos.update({"pudha@gmail.com": {"nome": "ELPUDHO"}}) #atualiza o dicionário -> se o primeiro dicionário tiver duas chaves, ele troca para o dicionário com 1 chave
                print(contatos)
                contatos.update({"aaaaa@gmail.com": {"nome": "Pudha1", "telefone": "3445-9932"}}) #atualiza o dicionário -> o primeiro dicionário tem uma chave, ele troca para o dicionário com duas chaves
                print(contatos)

#values
            if selecionar2 == 11:
                print("\nvalues")
                print(contatos)
                print(contatos.values()) #retorna todos os valores 

#in
            if selecionar2 == 12:
                print("\nin")
                print(contatos)
                print("pudha@gmail.com" in contatos)
                print("idade" in contatos)
                print("aaaa@gmail.com" in contatos)

#del
            if selecionar2 == 13:
                print("\ndel")
                print(contatos)
                del contatos["pudha@gmail.com"]["telefone"]
                print(contatos)
                del contatos["bbbbbb@gmail.com"]
                print(contatos)
