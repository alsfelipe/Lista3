alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alfabeto_codificado = ['k', 'q', 'f', 'm', 'x', 'e', 't', 'z', 'r', 'h', 'v', 'n', 'd', 'l', 'j', 'a', 's', 'u', 'y', 'b', 'g', 'w', 'p', 'o', 'i', 'c']
matriz = []
numero = int(input())
for i in numero:
    matriz.append([])
acao = ""
while acao != "FIM":
    acao = input()
    if acao == "adicionar":
        heroi_codificado = input()
        time = int(input())
        heroi_separado = heroi_codificado.split(" - ")
        matriz.insert([time], heroi_separado)


    if acao == "metamorfo":
        impostor = input()
        a = impostor.split("")
        for i in a:
            for k in alfabeto:
                if k == i:
                    indice_alfabeto = alfabeto.index(k)
                    