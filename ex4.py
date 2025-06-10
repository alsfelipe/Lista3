print("Go! Go! Power Rangers!")

niveis = []
tipo1 = []
tipo2 = []
tipo3 = []
nomes1 = []
nomes2 = []
nomes3 = []
zords = input()
zords = zords.split("-")
if "robocin" in zords:
    print("Os rangers encontraram o zord lendário!!!! O Robocin!!!! Eles não precisam mais de outros zords!")
else:
    for i in zords:
        if i.isnumeric():
            niveis.append(int(i))

    for n in niveis:
        if n <= 10:
            tipo1.append(n)
        elif n <= 30:
            tipo2.append(n)
        else:
            tipo3.append(n)

    #Ranger Vermelho
    if len(tipo1) > 0:
        maior_nivel = tipo1[0]

        for j in tipo1:
            if j > maior_nivel:
                maior_nivel = j

        vermelho = maior_nivel

        vermelho_nivel = str(vermelho)
        indice_vermelho = zords.index(vermelho_nivel)
        nome_vermelho = zords[indice_vermelho - 1]

        print(f"Zord do Ranger Vermelho: {nome_vermelho}")
        zord_vermelho = True
    else:
        print("Ranger Vermelho ficou sem zord!")

    #Nível Verde
    if len(tipo1) > 1:
        tipo1.remove(vermelho)
        segundo = tipo1[0]

        for k in tipo1:
            if k > segundo:
                segundo = k
            
        verde = segundo

        verde_nivel = str(verde)
        indice_verde = zords.index(verde_nivel)
        nome_verde = zords[indice_verde - 1]

        print(f"Zord do Ranger Verde: {nome_verde}")
        zord_verde = True
    else:
        print("Ranger Verde ficou sem zord!")

    #Nível Rosa
    if len(tipo2) > 0:
        maior_nivel = tipo2[0]

        for j in tipo1:
            if j > maior_nivel:
                maior_nivel = j

        rosa = maior_nivel

        rosa_nivel = str(rosa)
        indice_rosa = zords.index(rosa_nivel)
        nome_rosa = zords[indice_rosa - 1]

        print(f"Zord da Ranger Rosa: {nome_rosa}")
    else:
        print("Ranger Rosa ficou sem zord!")

    #Nível Preto
    if len(tipo2) > 1:
        tipo2.remove(rosa)
        segundo = tipo2[0]

        for k in tipo2:
            if k > segundo:
                segundo = k
            
        preto = segundo

        preto_nivel = str(preto)
        indice_preto = zords.index(preto_nivel)
        nome_preto = zords[indice_preto - 1]

        print(f"Zord do Ranger Preto: {nome_preto}")
    else:
        print("Ranger Preto ficou sem zord!")

    #Nível Azul
    if len(tipo3) > 0:
        maior_nivel = tipo3[0]

        for j in tipo3:
            if j > maior_nivel:
                maior_nivel = j

        azul = maior_nivel

        azul_nivel = str(azul)
        indice_azul = zords.index(azul_nivel)
        nome_azul = zords[indice_azul - 1]

        print(f"Zord do Ranger Azul: {nome_azul}")
    else:
        print("Ranger Azul ficou sem zord!")

    #Ranger Amarelo
    if len(tipo3) > 1:
        tipo3.remove(azul)
        segundo = tipo3[0]

        for k in tipo3:
            if k > segundo:
                segundo = k
            
        amarelo = segundo

        amarelo_nivel = str(amarelo)
        indice_amarelo = zords.index(amarelo_nivel)
        nome_amarelo = zords[indice_amarelo - 1]

        print(f"Zord da Ranger Amarelo: {nome_amarelo}")
    else:
        print("Ranger Amarelo ficou sem zord!")

