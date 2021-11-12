# Exercice 1

""" Ecrire la boucle for in range qui a la sortie suivante: """

"""
canari 1
canari 2
canari 3
canari 4
canari 5
"""

for i in range(1,6):
    print(f'canari {i}')

print("------------------------------------------------")

# Exercice 2

"""
Utilisez une boucle et la fonction "range" pour calculer la somme des 100 premier entier naturel
Utilisez la boucle while pour calculer le produit des 100 premiers entier naturel
"""

somme = 0
for i in range(1, 101):
    somme += i


b = 1
produit = 1
while b < 101:
    produit *= b
    b += 1

print("------------------------------------------------")

#Exercice 2:

""" Dans un fichier scipt, A l'aide de la fonction while et la fonction input (help(input)) écrivez cette blague
"Si repete et pepete sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?"
si la personne répond "repète", le programme pose la meme question : "Si repete et pepete sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?"
si la personne répond autre chose le programme pose comme question: "Mais non tu comprends pas, si repete et pepete sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste "
si la personne répond "tu es lourd" enfin le programme s'arrete """


answer = input("Si repete et pepete sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?  ")
end_program = False

while not end_program:
    if answer == "repète":
        answer = input("Si repete et pepete sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?  ")
    elif answer != "tu es lourd":
        answer = input("Mais non tu comprends pas, si repete et pepete sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste ?  ")
    else:
        end_program = True

print("------------------------------------------------")

#Exercice 3

"""Même exercice que le deux mais en utilisant break"""

while not end_program:
    if answer == "repète":
        answer = input("Si repete et pepete sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste?  ")
    elif answer != "tu es lourd":
        answer = input("Mais non tu comprends pas, si repete et pepete sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste ?  ")
    else:
        break

print("------------------------------------------------")

# Exercice 4

"""Ecrire un programme qui permet d'additioner les deux chiffres saisis par l'utilisateur"""

print("Quels nombres voulez-vous additionner ?")
program = True

a = input("Saisissez votre premier nombre    ")
b = input("Saisissez votre deuxième nombre    ")

while program:

    try:
        if type(float(a)) != str or type(float(b)) != str:
            print(float(a) + float(b))
            break

    except ValueError:

        print("Veuillez saisir des nombres valides    ")
        a = input("Saisissez votre premier nombre    ")
        b = input("Saisissez votre deuxième nombre    ")

print("------------------------------------------------")

# Mini projet

"""Creer une liste de course permettant d'effectuer toutes les options nécessaires à son utilisation"""


liste_course = ["poisson", "laitue", "poulet", "pommes", "poire", "lapin"]
program = True
retour = False
print("Choissisez une des options suivantes :\n 1: Ajouter un élèment à la liste\n 2: Retirer un élèment de la liste\n 3: Afficher la liste\n 4: Vider la liste\n 5: Quitter")

answer = input("Quel est votre choix?   ")

while program:
    if answer == "5":
        program = False
    elif answer == "4":
        liste_course = []
        print("Choissisez une des options suivantes :\n 1: Ajouter un élèment à la liste\n 2: Retirer un élèment de la liste\n 3: Afficher la liste\n 4: Vider la liste\n 5: Quitter")
        answer = input("Quel est votre choix?   ")
    elif answer == "3":
        print(liste_course)
        answer = input("Quel est votre choix?   ")
    elif answer == "2":
        print(liste_course)
        suppressed = input("Que voulez-vous supprimer ? (Tapez retour pour revenir en arrière)   ")
        while not retour:
            try: 
                if suppressed != "retour":
                    liste_course.remove(suppressed)
                    print(liste_course)
                    suppressed = input("Que voulez-vous supprimer ? (Tapez retour pour revenir en arrière)   ")
                else:
                    retour = True
            except ValueError:
                print("Supprimez un élément présent dans votre liste")
                print(liste_course)
                suppressed = input("Que voulez-vous supprimer ? (Tapez retour pour revenir en arrière)   ")
        retour = False
        print("Choissisez une des options suivantes :\n 1: Ajouter un élèment à la liste\n 2: Retirer un élèment de la liste\n 3: Afficher la liste\n 4: Vider la liste\n 5: Quitter")

        answer = input("Quel est votre choix?   ")

    elif answer == "1":
        ajout = input("Que voulez-vous ajouter ? (Tapez retour pour revenir en arrière)  ")
        while not retour:
            if ajout != "retour":
                liste_course.append(str(ajout))
                ajout = input("Que voulez-vous ajouter ? (Tapez retour pour revenir en arrière)   ")
            else:
                retour = True
        retour = False
        print("Choissisez une des options suivantes :\n 1: Ajouter un élèment à la liste\n 2: Retirer un élèment de la liste\n 3: Afficher la liste\n 4: Vider la liste\n 5: Quitter")
        answer = input("Quel est votre choix?   ")
    else:
        print("Veuillez saisir une valeur correcte   ")
        answer = input("Quel est votre choix?   ")