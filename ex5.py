print("Vamos lá, Vanellope! Vou te ajudar a montar um carro CINistro!")

lista = []
descartados = []
roda = ["",""]
corpo = ["",""]
volante = ["",""]
materiais_usados = []
carro = []
qualidade_carro = []

acabou = False
while not acabou:
    material = input()

    if material == "O REI DOCE ESTÁ ROUBANDO TODOS OS INGREDIENTES!":
        print("Ah não!! Ele vai destruir seu carro, Vanellope! CUIDADO")  
        descartados.append(roda[0])
        descartados.append(corpo[0])
        descartados.append(volante[0])
        roda = ["", ""]
        corpo = ["", ""]
        volante = ["", ""] 


    elif material == "Recursos Esgotados":
        acabou = True
    
    else:
        separar =  material.split(" - ")        
        doce = separar[0]
        qualidade = separar[1]
        materiais_usados.append([doce, qualidade])

        if doce == "Mentos" or doce == "Jujuba":

            if qualidade == "estragado":
                descartados.append(doce)

            elif qualidade == "alta qualidade":
                if roda[1] == "alta qualidade":
                    descartados.append(doce)
                else:
                    if roda[0] != "":
                        descartados.append(roda[0])
                    roda = [doce, qualidade]    

            elif qualidade == "qualidade mediana":
                if roda[1] == "alta qualidade" or roda[1] == "qualidade mediana":
                    descartados.append(doce)
                else:
                    if roda[0] != "":
                        descartados.append(roda[0])
                    roda = [doce, qualidade]
        
        elif doce == "Bolo de rolo" or doce == "Barra de chocolate" or doce == "Banda de ovo de Páscoa":

            if qualidade == "estragado":
                descartados.append(doce)
            
            elif qualidade == "alta qualidade":
                if corpo[1] == "alta qualidade":
                    descartados.append(doce)
                else:
                    if corpo[0] != "":
                        descartados.append(corpo[0])
                    corpo = [doce, qualidade]
            
            elif qualidade == "qualidade mediana":
                if corpo[1] == "alta qualidade" or corpo[1] == "qualidade mediana":
                    descartados.append(doce)
                else:
                    if corpo[0] != "":
                        descartados.append(corpo[0])
                    corpo = [doce, qualidade]
            
        
        elif doce == "Pretzel" or doce == "Donuts":

            if qualidade == "estragado":
                descartados.append(doce)

            elif qualidade == "alta qualidade":
                if volante[1] == "alta qualidade":
                    descartados.append(doce)
                else:
                    if volante[0] != "":
                        descartados.append(volante[0])
                    volante = [doce, qualidade]
            
            elif qualidade == "qualidade mediana":
                if volante[1] == "alta qualidade" or volante[1] == "qualidade mediana":
                    descartados.append(doce)
                else:
                    if volante[0] != "":
                        descartados.append(volante[0])
                    volante = [doce, qualidade]
        
       
carro.append(roda[0])
carro.append(corpo[0])
carro.append(volante[0])
qualidade_carro.append(roda[1])
qualidade_carro.append(corpo[1])
qualidade_carro.append(volante[1])
if carro and carro[0] == "":
    carro.pop(0)
if carro and carro[1] == "":
    carro.pop(1)
if carro and carro[2] == "":
    carro.pop(2)
if qualidade_carro[0] == "qualidade mediana" and qualidade_carro[1] == "qualidade mediana" and qualidade_carro[2] == "qualidade mediana":
    print("Pelo menos anda! Você consegue!")

elif (qualidade_carro[0] == "alta qualidade" or qualidade_carro[1] == "alta qualidade" or qualidade_carro[2] == "alta qualidade") and len(carro) == 3:
    print("Conseguimos! Impossível você não ganhar essa corrida, Vanellope!")
    print(f"Para fazer o carro você utilizou {corpo[0]} para ser a estrutura do carro, {volante[0]} para o volante, {roda[0]} para compor as rodas!")

if len(carro) < 3:
    print("Sinto muito, Vanellope. Não consegui te ajudar dessa vez.")

if descartados:
    a = ", ".join(descartados)
    print("Alguns doces foram descartados. São eles:")
    print(a)
