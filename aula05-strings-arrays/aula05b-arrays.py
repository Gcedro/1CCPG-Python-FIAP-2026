lista_frutas = ["Banana", "Maça", "Morango"]

# lista_frutas[0] = "Banana"
# lista_frutas[1] = "Maça"
# lista_frutas[2] = "Morango"
print(lista_frutas[1])

lista_frutas.append("Pera")
print(lista_frutas)

qtd_frutas = len(lista_frutas)
print("qtd de frutas", qtd_frutas)

# FOR INDEXADO para PERCORRER
for i in range(qtd_frutas):
    print(lista_frutas[i])

print()

# FOR EACH em PYTHON
for fruta in  lista_frutas:
    print(fruta)


numeros = [0,5,11,4]
for numero in numeros:
    print(numero)