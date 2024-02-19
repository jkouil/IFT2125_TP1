#Nom, Matricule
#Nom, Matricule

import math
import sys
INFINITY = math.inf

#Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier, 
#faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
#d'autres librairies.
#Functions to read/write in files. you can modify them, do some parsing,
#add a return value, but don't use other librairies
def read_problems(input_file):
    # lecture du fichier/file reading

    with open(input_file) as file:
        # Avance l'itérateur de 2 lignes
        n = next(file) #nombre de problemes

        liste_coordonnees = [] # tous les coordonnees, liste des listes
        for i in range(int(n)):
            nombreSommets = next(file)
            coordonnees = [] #coordonnes du probleme i, liste des [float, float]
            for j in range(int(nombreSommets)):
                line = next(file)
                float_list = list(map(float, line.strip().split(" ")))
                coordonnees.append(float_list)
            liste_coordonnees.append(coordonnees)
        return (liste_coordonnees, n)

def write(fileName, listResult):
    #écrire la sortie dans un fichier/write output in file
    file = open(fileName, "w")
    for content in listResult:
        file.write(str(content))
        file.write("\n")

    file.close()




#Fonction main/Main function
def main(args):
    input_file = args[0]
    output_file = args[1]
    #TODO : Continuer ici/Complete here...
    #Vous pouvez découper votre code en d'autres fonctions...
    #You may split your code in other functions...

    def distance(x1, y1, x2, y2):
        dx = x1 - x2
        dy = y1 - y2
        return math.sqrt(dx ** 2 + dy ** 2)


    def take_dis(elems): #input: list_coordonnees, output: distance
        return elems[0]

    def take_arete(elems): #input: liste_coordonnes, ouput: sommets lies par l'arete
        return (elems[1],elems[2])

    def check_distinct(arete, listeArbres):
        #verifie si les sommets de l'arete est dans le meme arbre
        for arbre in listeArbres:
            s1 = arete[0]
            s2 = arete[1]

            if s1 in arbre and s2 in arbre:
                return False # sommets dans le meme arbre

        return True # non trouve

    def accepter_arete(listeArbres, arete): #accepter un arete en liant deux arbres
        arbre1 = set() #deux arbres a connecter
        arbre2 = set()

        for arbre in listeArbres:
            s1 = arete[0]
            s2 = arete[1]

            if s1 in arbre:
                if arbre1 == set():
                    arbre1.update(arbre)

                else: arbre2.update(arbre)

            if s2 in arbre:
                if arbre1 == set():
                    arbre1.update(arbre)
                else: arbre2.update(arbre)

        listeArbres.remove(arbre1) # enlever les arbres
        listeArbres.remove(arbre2)

        arbre1.update(arbre2) #ajoute nouveau
        listeArbres.append(arbre1)

    def kruskal(listeArbres, listeAretes, dictAretes): #input: liste des arbres d'un elements et une liste d'aretes
        distanceTotal = 0
        for arete in listeAretes:
            if check_distinct(arete, listeArbres): # sommets ne sont pas dans meme arbre
                accepter_arete(listeArbres, arete)
                distanceTotal += dictAretes[arete]

        if (len(listeArbres) != 1):
            distanceTotal = False

        return distanceTotal

    def trouver_disTotal(coordonnees):
        liste_coordonnees = []
        set_sommets = set()  # un set des sommets, aussi un set des arbres distincts

        for i in range(len(coordonnees)):
            for j in range(i + 1, len(coordonnees)):
                liste_coordonnees.append(
                    [distance(coordonnees[i][0], coordonnees[i][1], coordonnees[j][0], coordonnees[j][1]),
                     f"S{i}", f"S{j}"])  # [tuple distance, sommet1,sommet2]
                set_sommets.add(f"S{i}")
                set_sommets.add(f"S{j}")
        liste_sommets = list(set_sommets)

        liste_coordonnees.sort(key=take_dis)
        liste_aretes = []  # liste des aretes ordonnees selon le poids
        dict_arete = {}  # dict de arete: dis
        for coor in liste_coordonnees:
            arete = take_arete(coor)
            liste_aretes.append(arete)
            dis = take_dis(coor)
            dict_arete.update({arete: dis})

        liste_arbres = []  # une liste des sets des arbres
        for sommet in liste_sommets:
            liste_arbres.append({sommet})

        return kruskal(liste_arbres, liste_aretes,dict_arete)

    # Nous avons implementer l'algo krustal car le graphe est complet, prim nous obligerait de faire le calcul a chaque
    # iteration

    result = read_problems(input_file)  # les sommets(x,y) coordonnes
    liste_coordonnees = result[0]
    nombre_problemes = result[1]
    liste_resultat = []

    for i in range(int(nombre_problemes)):
        distanceTotal = trouver_disTotal(liste_coordonnees[i])
        approximation = round(distanceTotal, 3)
        liste_resultat.append(approximation)

    write(output_file, liste_resultat)


#NE PAS TOUCHER
#DO NOT TOUCH
if __name__ == '__main__':
    main(sys.argv[1:])
