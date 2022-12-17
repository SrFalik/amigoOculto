from random import shuffle
from random import randint
from criarLista import criarLista


def sortear():
    listaJogadores = criarLista()
    shuffle(listaJogadores)
    listaJogadoresCopia = listaJogadores.copy()
    lenLista = len(listaJogadores)
    listaResultado = []
    for i in range(lenLista):
        while True:
            r = randint(0, len(listaJogadores) - 1)
            r2 = randint(0, len(listaJogadoresCopia) - 1)
            if listaJogadores[r] != listaJogadoresCopia[r2]:
                print(listaJogadores[r]["nome"] + " tirou " + listaJogadoresCopia[r2]["nome"])
                resultado = {
                    "r": listaJogadores[r],
                    "r2": listaJogadoresCopia[r2]
                }
                listaResultado.append(resultado)
                listaJogadores.pop(r)
                listaJogadoresCopia.pop(r2)
                break
            else:
                continue
    return listaResultado
