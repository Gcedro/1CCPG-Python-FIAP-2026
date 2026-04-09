#escolha do usuário
#0 --> sair do programa
#1 --> entrar no programa
# ---> erro!

escolha_usuario = 1123123

match escolha_usuario:
    case 0:
        print("sair do programa")
    case 1: 
        print("entrar no programa")
    case _:
        print("Erro!")
