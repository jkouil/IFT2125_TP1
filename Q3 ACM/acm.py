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
    acm = 0
    def distance(x1, y1, x2, y2):
        dx = x1 - x2
        dy = y1 - y2
        return math.sqrt(dx ** 2 + dy ** 2)
    #Nous avons implementer l'algo krustal car le graphe est complet, prim nous obligerait de faire le calcul a chaque
    #iteration

    input_file = args[0]
    output_file = args[1]
    coordonnees = read_problems(1,"./Q3 ACM/"+input_file)
    visited= []

    liste_coordonnees=[]
    for i in range(len(coordonnees)):
        k= i +1
        for j in range(k, len(coordonnees)):
            liste_coordonnees.append([distance(coordonnees[i][0],coordonnees[i][1],coordonnees[j][0], coordonnees[j][1]),
                                f"S{i}", f"S{j}" ])
    print("-----------------------------------")
    breakpoint()
    def takeFirst(elem):
        return elem[0]

    liste_coordonnees = sorted(liste_coordonnees, key=takeFirst)

    for x in liste_coordonnees:
        if len(visited) < len(coordonnees):
            if x[2] in  visited  and x[1] in visited:
                continue
            else:
                acm = acm + x[0]
                for i in range(1,3):
                    if x[i] not in visited:
                        visited.append(x[i])
                        print(len(visited))
        else:
            break
    print(acm)

#NE PAS TOUCHER
#DO NOT TOUCH
if __name__ == '__main__':
    main(sys.argv[1:])
