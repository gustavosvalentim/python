from time import sleep

#Comandos
comandos = {
        "i":"iventario",
        "c":"lista de craft",
        "s":"sair",
        "craft [item]":"craft um item",
}

#Inventario
itens = {
        "graveto":10,
        "fosforo":5,
        "pedra":1,
        "madeira":1,
        "fogueira":0,
        "comida":2,
}

#Craft
craft = {
        "fogueira":{"graveto":5, "fosforo":1},
}


print("#Jogo de sobrevivencia feito em python.")
print("\n")

print("      #Inicio")
beginning = "#Faça uma fogueira."
for i in range(len(beginning)):
    sleep(0.3)
    print(beginning[i % len(beginning)], end="", flush=True)

print("\n")
print("#\"?\" para ver os comandos")
while True:
    comando = input(" > ").split()
    if len(comando) > 0:
        acao = comando[0].lower()
    if len(comando) > 1:
        acao = comando[0].lower()
        item = comando[1].lower()

    if acao == "?":
        for key in comandos:
            print(key + " : " + comandos[key])
        print("\n")

    if acao == "s":
        exit()

    if acao == "c":
        for key in craft:
            print("{} : {}".format(key, craft[key]))
        print("\n")

    if acao == "i":
        for key in itens:
            print("{} : {}".format(key, itens[key]))
        print("\n")

    if acao == "craft":
        for key in craft:
            if item == key:
                opcao = input("Voce deseja fazer um(a)" + key + "?")
                opcao = opcao.lower()
                if opcao == "sim" or opcao == "s":
                    continue
                elif opcao == "nao" or opcao == "n":
                    continue
