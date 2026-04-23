for cp in range(3):
    print(f"Produto {cp}")

# de 1 a 10, pulando de 2 em 2
for i in range (1, 11, 2):
    print (1)

# ATIVIDADE 3
qtd_produtos = int(input("Digite a qtd de produtos: "))

for i in range(qtd_produtos):
    print(f"Produto {i+1}")

# LAÇOS ALINHADOS -
# ESTRUTURA DE REP. ENCADEADA

for i in range(9,4):
    for j in range (8,3,2):
        print(f"i:{i}, j:{j}")