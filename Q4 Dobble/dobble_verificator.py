# Nom, Matricule
# Nom, Matricule

# cette classe sert a verifier la validite de l'ensemble des cartes du jeu dans le fichier cartes.txt
# this class is used to check the validity  of the game cards set in the cartes.txt file

# doit retourner 0 si tout est correct, 1 si le jeu n'est pas optimal selon l'ordre et 2 si le jeu n'est pas valide
# should return 0 if everything is correct, 1 if the game set is not optimal according to the order and 2 if the game set is invalid

# import os.path

class Verificator():
    def __init__(self):
        pass

    def verify(self, cards_file="cartes.txt", verbose=False):
        if verbose:
            print("***Verification des cartes***")

        # TODO
        # a completer
        def check2cards(paires):
            it = iter(paires)
            for paireCard in it:

                card1 = paireCard[0]
                card2 = paireCard[1]
                same_sym = 0  # nb de symbols identiques
                for sym in card1:
                    if sym in card2:
                        same_sym += 1
                if same_sym != 1:
                    # print(card1,card2,same_sym)
                    return False

            return True

        all_sym = set()
        with open(cards_file) as file:
            game = []
            for line in file:
                symbol_list = list(map(float, line.strip().split(" ")))
                game.append(symbol_list)
                all_sym.update(symbol_list)
            file.close()
        n = len(game[0]) - 1  # l'ordre du jeu

        # test : le nombre de carte devrait être optimal
        test1 = False
        nb_carte = len(game)
        nb_expected = n ** 2 + n + 1
        if nb_carte == nb_expected:
            test1 = True

        # test : le nombre de symboles par carte est le même pour chaque carte
        test2 = True
        nombreSymb = len(game[0])
        for card in game:
            if nombreSymb != len(card):
                test2 = False

        # test : chaque paire de cartes partagent toujours un et un seul symbole en commun
        test3 = False
        pairesCards = [(card1, card2) for card1 in game for card2 in game if card1 != card2]
        if check2cards(pairesCards):
            test3 = True

        # test : le nombre de symbole total devrait être optimal
        nb_total = len(all_sym)
        test4 = False
        if (nb_total == nb_expected):
            test4 = True

        # test: the number of cards should be optimal
        # test: the number of symbols per card is the same for each card
        # test: each pair of cards always shares one and only one symbol in common
        # test: the total number of symbols should be optimal

        if not test2 or not test3: return 2
        if not test1 or not test4: return 1

        # succes (0) si le jeu est valide et optimal
        # avertissement (1) si le jeu de carte n'est pas optimal
        # erreur (2) si le jeu de carte n'est pas valide

        # success (0) if the game is valid and optimal
        # warning (1) if the card game is not optimal
        # error (2) if the card set is invalid
        return 0


