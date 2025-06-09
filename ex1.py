acabou = False
while acabou == False:
    fazer = input()
    compras = []
    if fazer == "Anotar ingrediente":
        ingediente_anotado = input()
        compras.append(ingediente_anotado)
    elif fazer == "Ingrediente Urgente!":
        ingrediente_urgente = input()
        compras.insert(0, ingrediente_urgente)
    elif fazer == "Saci disse que já tem":
        remover = input()
        compras.remove(remover) 
    elif fazer == "Saci trocou a ordem":
        ingrediente_atual = input()
        ingrediente_final = input()
        compras.insert(ingrediente_final, ingrediente_atual)
        compras.remove(ingrediente_atual)
        compras.append(ingrediente_atual)
    elif fazer == "Organizar a lista":
        ingrediente1 = input()
        ingrediente2 = input()
        local_ingrediente1 = compras.index(ingrediente1)
        local_ingrediente2 = compras.index(ingrediente2)
        compras.remove(ingrediente1)
        compras.remove(ingrediente2)
        compras.insert(local_ingrediente1, ingrediente2)
        compras.insert(local_ingrediente2,local_ingrediente1)
    elif fazer == "Deixar para depois":
        ingrediente_depois = input()
        compras.remove(ingrediente_depois)
        compras.append(ingrediente_depois)
    elif fazer == "Ler a lista para a vovó":
        for i in compras:
            print(i, end=", ")
    elif fazer == "E por hoje é só, pessoal!":
        acabou = True
for i in compras:
    print("Pronto, vovó! A lista de compras para o bolo de Narizinho está pronta. Podemos ir ao mercado. A lista final é: ", end=f"{compras}, ")