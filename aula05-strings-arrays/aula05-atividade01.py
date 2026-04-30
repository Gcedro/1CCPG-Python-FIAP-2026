'''nomes = ["Lucas", "Matheus", "Leonardo", "Guilherme"]
qtd_nomes = len(nomes)
print(nomes)

for i in range(qtd_nomes):
    for j in range(qtd_nomes):
        if i == j or i < j:
            continue
        print(nomes[i], nomes[j])'''


nomes = ["Lucas", "Matheus", "Leonardo", "Guilherme"]

for i in range(len(nomes)):
    for j in range(len(nomes)):
        print(nomes[i], nomes[j])
    print()

