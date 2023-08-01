while True:
    numero = int(input("Informe um número: "))

    if numero == 10: #Para se digitar o número 10
        break
    print(numero)

for numero in range(15):
    #!!!break antes do continue, caso ambos atendam à condição, pulará o break.
    if numero == 12: #Para no 11. 
        break 
    
    if numero == 10: #Pula o número 10
        continue
    
    print(numero, end =" ")

print()

#Exemplo números ímpar
for numero in range(100):
    if numero % 2 == 0: #pula os números pares
        continue
    print(numero, end=" ")