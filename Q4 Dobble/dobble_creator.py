#Nom, Matricule
#Nom, Matricule

# cette classe sert a créer les cartes visuelles du jeu dans le dossier "results"
# this class is used to create the game visual cards in the "results" folder

from PIL import Image
import os
import math
import random

# info :
# https://pillow.readthedocs.io/en/stable/reference/Image.html

class Creator():
    def __init__(self, pic_size=300, border_size=10):
        self.pic_size = pic_size
        self.border_size = border_size

    def make_cards(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Creation des cartes visuelles***")

        #imagesFile = [file for file in os.listdir('images') if file.endswith('.png')] #liste de images dans "images"
        prefixedPath = 'images/'

        with open(cards_file) as file:
            game = []
            for line in file:
                symbol_list = list(map(float, line.strip().split(" ")))
                game.append(symbol_list)

            file.close()

        n = len(game[0])
        nb_lignes = n // 3 + 1 # nombre d'images par ligne
        nb_colonne = nb_lignes
        path_final = 'results/'
        grandeur = int((self.pic_size//nb_lignes))
        idx = 0

        def image_create(symbolImages,idx):  # resultat = path des resultats crees
            image = Image.new('RGB', (self.pic_size, self.pic_size),(256,256,256))
            i = 0
            placement = self.pic_size // nb_lignes
            listPlacement = [(x,y) for x in range(0,self.pic_size, placement) for y in range(0, self.pic_size, placement)]

            for symbol in symbolImages:
                pos = listPlacement[i]
                symbol = symbol.resize((grandeur,grandeur))

                image.paste(symbol, pos)

                p = path_final + 'card' + str(idx+1) + '.png'


                i += 1
            return image.save(p)


        for card in game:

            cardImages = []
            for sym in card:
                imageName = str(int(sym)) + '.png'
                path = prefixedPath + imageName

                im = Image.open(path)

                im.convert('RGBA')
                angle = random.random()
                angle = angle * 360


                im = im.rotate(angle,fillcolor = 'white')
                cardImages.append(im)

            image_create(cardImages,idx)

            idx += 1
            print(idx)



            #print(cardImages)



        # TODO
        # a completer


        # lecture des images à partir du dossier "images" : "1.png2, "2.png", "3.png", ... "<N>.png"
        # placement des images sur les cartes visuelles, rotations apreciees
        # ajout de la bordure sur les cartes visuelles
        # sauvegarde des cartes dans le dossier "results" : "card1.jpg", "card2.jpg", "card3.jpg", ... "card<N>.jpg"
            
        # reading images from the "images" folder: "1.png2, "2.png", "3.png", ..., "<N>.png"
        # placement of images on visual cards, rotations appreciated
        # added border on visual cards
        # save cards in the “results” folder : "card1.jpg", "card2.jpg", "card3.jpg", ... "card<N>.jpg"

if __name__ == '__main__':
    c = Creator()
    c.make_cards(cards_file = "cartes.txt",verbose = False)