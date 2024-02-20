# Qiwu Wen, Matricule
# Nom, Matricule

# cette classe sert a créer les cartes du jeu dans le fichier cartes.txt
# this class is used to create the game cards in the cartes.txt file

import random  # pour le melange des symboles sur chaque carte # for mixing symbols on each card

import dobble_verificator


class Generator():

    def __init__(self, order=7):
        self.order = order

    def generate(self, cards_file="cartes.txt", verbose=False):
        if verbose:
            print("***Generation des cartes***")

        # TODO
        # a completer
        def add_horizon(horizon, sym):
            if len(horizon[n]) == n:  # dernier chiffre est rempli
                for elem in horizon:
                    elem.append(sym)  # ajoute symbol au n ieme elements
            for elem in horizon:
                if len(elem) < n:  # on peut encore ajouter symbol au carte
                    elem.append(sym)

                    return

        def lists_verticals(n):
            #retourner des listes des points(x,y) qui sont dans
            #les memes lignes verticales
            resultat = []
            for x in range(n):
                ligneX = []
                for y in range(n):
                    pos = (x,y)
                    ligneX.append(pos)
                resultat.append(ligneX)
            return resultat

        def lists_horizontals(n):
            #retourner des listes des points(x,y) qui sont dans
            #les memes lignes horizontales
            resultat = []
            for y in range(n):
                ligneY = []
                for x in range(n):
                    pos = (x,y)
                    ligneY.append(pos)
                resultat.append(ligneY)
            return resultat

        def lists_directions(n, pente):
            resultat = []
            for degree in range(n):
                dListe = []
                for x in range(n):
                    pos = (x, (pente * x + degree) % n)
                    dListe.append(pos)

                resultat.append(dListe)
            return resultat

        def mettre_syms(n,symbols,dictCartes, horizon):
            listVer = lists_verticals(n)
            listHor = lists_horizontals(n)

            for ver in listVer:
                sym = symbols.pop()
                add_horizon(horizon,sym)
                for position in ver:
                    if position not in dictCartes.keys():
                        dictCartes[position] = []
                    dictCartes[position].append(sym)

            for pente in range(1,n):
                listPenteN = lists_directions(n,pente)
                for list in listPenteN:
                    sym = symbols.pop()
                    add_horizon(horizon, sym)

                    for position in list:
                        if position not in dictCartes.keys():
                            dictCartes[position] = []
                        dictCartes[position].append(sym)

            for hor in listHor:
                sym = symbols.pop()
                add_horizon(horizon, sym)
                for position in hor:
                    if position not in dictCartes.keys():
                        dictCartes[position] = []
                    dictCartes[position].append(sym)

            add_horizon(horizon,symbols.pop())
            return dictCartes

        # melange aleatoire des symboles sur les cartes,
        # pour ne pas avoir des répétitions de symboles sur les mêmes endroits des cartes
        # random mixing of symbols on the cards,
        # so as not to have repetitions of symbols on the same places on the cards

        def melanger(symbols):
            random.shuffle(symbols)
            return

        # ecriture des cartes dans le fichier cards_file
        # writing cards in the cards_file file
        def write(fileName, dictCartes,horizon):
            file = open(fileName, "w")

            for position in dictCartes: #position = carte
                symbs = dictCartes[position] # liste des symbols par chaque carte
                melanger(symbs)
                for symb in symbs:
                    file.write(str(symb) + " ")
                file.write("\n")
            for card in horizon:
                melanger(card)
                for sym in card:
                    file.write(str(sym) + " ")
                file.write("\n")
            file.close()

        n = self.order

        nombreTotal = n ** 2 + n + 1

        dictCartes = dict() # dict (i,j): carte[symbols]
        horizon = [[] for _ in range(n+1)]  # tableau horizon [n+1]
        symbols = [i+1 for i in range(nombreTotal)]  # tableau des symboles de longeur n**2 + n + 1
        melanger(symbols)
        # random.shuffle(symbols)
        mettre_syms(n,symbols,dictCartes,horizon)

        write(fileName="cartes.txt", dictCartes = dictCartes,horizon=horizon)




      #  add_horizon(horizon, symbols)  # ajoute dernier elems du symbols au horizon

       # print(horizon)


        # TODO
        # a completer



        # TODO
        # a completer


