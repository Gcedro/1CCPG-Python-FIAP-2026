aluno = {
    "nome": "Guilherme",
    "idade": 18,
    
}

aluno["nome"] = "João"
print(aluno["nome"])

aluno["cidade"] = "São Paulo"
print(aluno["cidade"])


for chave, valor in aluno.items():
    print(chave, valor)

