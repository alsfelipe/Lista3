acabou = False
nome = []
hora = []
local = []
testemunha = []
locais_invalidos = []
horas_invalidas = []
suspeito_seguranca = []
suspeito_testemunha = []
j = []
seguranca_baixa = ["Catacumbas de Paris", "Parque dos Príncipes", "Padaria Dupain Cheng"]
locais_permitidos = ["Torre Eiffel", "Museu do Louvre", "Catacumbas de Paris", "Biblioteca Nacional", "Galeria Lafayette", "Parque dos Príncipes", "Catedral de Notre-Dame", "Jardim de Luxemburgo", "Padaria Dupain Cheng"]
for n in range(6):
    suspeito = input()
    a = suspeito.split(" - ")
    nome.append(a[0])
    hora.append(a[1])
    local.append(a[2])
    testemunha.append(a[3])

for i in local:
    indice = local.index(i)
    if not i in locais_permitidos:
        locais_invalidos.append(i)
        acabou = True
if not acabou:
    for i in local:
        indice = local.index(i)
        if i == "Torre Eiffel":
            abre = "09:00"
            fecha = "23:00"
            if not abre <= hora[indice] <= fecha:
                horas_invalidas.append(hora[indice])
                j.append(indice)
        elif i == "Museu do Louvre":
            abre = "08:00"
            fecha = "18:00"
            if not abre <= hora[indice] <= fecha:
                horas_invalidas.append(hora[indice])
                j.append(indice)
        elif i == "Catacumbas de Paris":
            abre = "10:00"
            fecha = "20:00"
            if not abre <= hora[indice] <= fecha:
                horas_invalidas.append(hora[indice])
                j.append(indice)
        elif i == "Biblioteca Nacional":
            abre = "07:00"
            fecha = "22:00"
            if not abre <= hora[indice] <= fecha:
                horas_invalidas.append(hora[indice])
                j.append(indice)
        elif i == "Galeria Lafayette":
            abre = "10:00"
            fecha = "21:00"
            if not abre <= hora[indice] <= fecha:
                horas_invalidas.append(hora[indice]) 
                j.append(indice)   
        elif i == "Parque dos Príncipes":
            abre = "06:00"
            fecha = "23:00"
            if not abre <= hora[indice] <= fecha:
                horas_invalidas.append(hora[indice])   
                j.append(indice)
        elif i == "Catedral de Notre-Dame":
            abre = "08:00"
            fecha = "18:30"
            if not abre <= hora[indice] <= fecha:
                horas_invalidas.append(hora[indice])
                j.append(indice)   
        elif i == "Jardim de Luxemburgo":
            abre = "07:00"
            fecha = "19:00"
            if not abre <= hora[indice] <= fecha:
                horas_invalidas.append(hora[indice])   
                j.append(indice)
        elif i == "Padaria Dupain Cheng":
            abre = "04:00"
            fecha = "20:00"
            if not abre <= hora[indice] <= fecha:
                horas_invalidas.append(hora[indice])
                j.append(indice)
    
    if not (locais_invalidos or horas_invalidas):
        for k in range(6):
            if local[i] in seguranca_baixa:
                suspeito_seguranca.append(nome[i])
    if not suspeito_seguranca:
        for x in range(6):
            if testemunha[x] == "nenhuma":
                suspeito_testemunha.append(nome[x])
    if not suspeito_testemunha:
        print("Poxa vida, todos os àlibis parecem válidos… mas algo continua errado")
    
    tamanho_hora = len(horas_invalidas)
    tamanho_seguranca = len(suspeito_seguranca)
    tamanho_testemunhas = len(suspeito_testemunha)

    if len(horas_invalidas) == 1:
        
