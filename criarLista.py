def criarLista():
        qtd = int(input("Digite a quantidade de jogadores: "))
        listaJogadores = []
        for i in range(qtd):
            nome = str(input("Digite o nome do jogador #" + str(i + 1) + ": "))
            while True:
                numero = str(input("Digite o numero do jogador #" + str(i + 1) + " (ex: +5521945648104): "))
                if len(numero) != 14:
                    print("Numero invalido")
                else:
                    break
            jogador = {
                "nome": nome,





                "numero": numero
            }
            listaJogadores.append(jogador)
        return listaJogadores
