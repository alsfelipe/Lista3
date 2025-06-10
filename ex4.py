print("Go! Go! Power Rangers!")

niveis = []
tipo1 = []
tipo2 = []
tipo3 = []
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
vermelho = max(tipo1)
tipo1.remove(vermelho)
vermelho_nivel = zords.index(vermelho)
vermelho_lugar = zords[vermelho_nivel - 1]
print(zords[vermelho_nivel - 1])
#Nível Verde
verde = max(tipo1)

#Nível Rosa
rosa = max(tipo2)
tipo2.remove(rosa)

#Nível Preto
preto = max(tipo3)
tipo3.remove(preto)

#Nível Azul
azul = max(tipo3)

