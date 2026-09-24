palavras = {
    "frutas": ["banana", "morango", "abacaxi", "melancia"],
    "cores": ["azul", "verde", "amarelo", "vermelho"],
    "animais": ["cachorro", "gato", "elefante", "girafa"]
}

print("================================")
print("      JOGO DA ADIVINHAÇÃO")
print("================================")
print()

# Mostrar as categorias
print("Escolha uma categoria:")

categorias = list(palavras.keys())

for i in range(len(categorias)):
    print(f"{i + 1} - {categorias[i]}")

opcao = int(input("Digite a opção: "))

# Escolher a categoria
categoria = categorias[opcao - 1]

print()
print(f"Categoria escolhida: {categoria}")

# Pegar as palavras da categoria escolhida
lista_palavras = palavras[categoria]

print(f"Essa categoria possui {len(lista_palavras)} palavras.")

print()

# Mostrar as palavras disponíveis
print("Escolha a posição da palavra:")

for i in range(len(lista_palavras)):
    print(f"{i + 1} - Palavra {i + 1}")

posicao = int(input("Digite a posição: "))

# Pegar a palavra escolhida
palavra = lista_palavras[posicao - 1]

# Esconder a palavra
palavra_oculta = ["_"] * len(palavra)

# Número de tentativas
tentativas = 6

print()
print("================================")
print("        JOGO COMEÇOU!")
print("================================")

while tentativas > 0 and "_" in palavra_oculta:

    print()
    print("Palavra:", " ".join(palavra_oculta))
    print("Tentativas restantes:", tentativas)

    letra = input("Digite uma letra: ").lower()

    # Verificar se a letra existe
    if letra in palavra:

        print("Você acertou a letra!")

        # Revelar todas as posições da letra
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_oculta[i] = letra

    else:

        print("Você errou!")
        tentativas -= 1


# Resultado 
print()

if "_" not in palavra_oculta:

    print("================================")
    print("          PARABÉNS!")
    print("================================")
    print(f"Você descobriu a palavra: {palavra}")

else:

    print("================================")
    print("        VOCÊ PERDEU!")
    print("================================")
    print(f"A palavra era: {palavra}")