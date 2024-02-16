#Nom, Matricule
#Nom, Matricule

import math
import sys
INFINITY = math.inf


#Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier, 
#faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
#d'autres librairies.
#Functions to read/write in files. you can modify them, do some parsing,
#add a return value, but don't use other librairiesr
def read_problems(problems, input_file):
    # lecture du fichier/file reading
    coordonnees = []
    with open(input_file) as file:
    # Avance l'itérateur de 2 lignes
        next(file)
        next(file)
        for line in file:
            line= list(map(float, line.strip().split(" ")))
            coordonnees.append(line)
        return coordonnees

def write(fileName, content):
    #écrire la sortie dans un fichier/write output in file
    file = open(fileName, "w")
    file.write(content)
    file.close()


#Fonction main/Main function
def main(args):
    global acm
    global connected
    global ens_connexion
    ens_connexion=[set([])]
    connected=[]
    acm = 0

    def distance(x1, y1, x2, y2):
        dx = x1 - x2
        dy = y1 - y2
        return math.sqrt(dx ** 2 + dy ** 2)
    #Nous avons implementer l'algo krustal car le graphe est complet, prim nous obligerait de faire le calcul a chaque
    #iteration

    input_file = args[0]
    output_file = args[1]
    coordonnees = read_problems(1,input_file)
    liste_coordonnees=[]
    for i in range(len(coordonnees)):
        for j in range(i +1, len(coordonnees)):
            liste_coordonnees.append([distance(coordonnees[i][0],coordonnees[i][1],coordonnees[j][0], coordonnees[j][1]),
                                f"S{i}", f"S{j}" ])
    def takeFirst(elem):
        return elem[0]

    def taille_set(ensemble):
        return -len(ensemble)

    def connexion(liste):
        tmp = set(liste)
        compteur = 0
        for x in ens_connexion:
            inter = len((tmp & x))
            if inter == 1:
                ens_connexion[ens_connexion.index(x)] = x.union(tmp)
                #ens_connexion.sort(key=taille_set)
                return True
            elif inter == 2:
                if compteur > 0 :
                    ens_connexion[:compteur]
                return False
            else:
                ens_connexion.append(tmp)
                compteur += 1
                #ens_connexion.sort(key=taille_set)
                #return True

    liste_coordonnees = sorted(liste_coordonnees, key=takeFirst)

    #ajoute les premiers elements dans la liste connecte
    #connected.append(liste_coordonnees[0][1])

    for i in range (len(liste_coordonnees)):
        x = liste_coordonnees[0]
        if len(ens_connexion[0]) < len(coordonnees):
            add = connexion(x[1:])
            if add == True :
                acm = acm + x[0]
            liste_coordonnees.pop(0)
        else:
            break


    write(output_file,str(acm))

#NE PAS TOUCHER
#DO NOT TOUCH
if __name__ == '__main__':
    main(sys.argv[1:])
