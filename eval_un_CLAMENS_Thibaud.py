# CLAMENS Thibaud 1g3

# Exercice A

def salaire_hebdo(paye_heure : int, heures : int) -> int:
    """
    Calcule le salaire hebdomadaire en fonction du salaire à l'heure et du nombre d'heures de travail
    """
    if (heures <= 35):
        return heures*paye_heure
    else:
        return 35*paye_heure + (heures - 35)*paye_heure * 1.5
    
"""nom = input("Veuillez entrer le nom du salarié : ")
h = int(input(f"Entrer le nombre d'heures effectuées par {nom} dans cette semaine : "))
s = int(input(f"Entrer les salaire horaire de {nom} : "))
print(f"La paye de {nom} est {salaire_hebdo(s, h)}")"""

#Exercice B
op_valides = ["+", "-", "*", "/"]

def operation( a : float, b : float, op : str) -> float:
    """
    Renvoie l'opération de a par b en fonction de l'opérateur op
    """
    if (op == "+"):
        return a+b
    elif (op == "-"):
        return a-b
    elif (op == "*"):
        return a*b
    elif (op == "/"):
        return a/b
    else : raise ValueError("L'opérateur entré n'est pas correct")
    
"""a = float(input("Entrer le nombre 1 : "))
op = input("Entrer l'opération (+, - , * ,/ )")
while (op not in op_valides):
      print("L'opérateur est incorrect, veuillez choisir entre +, -, *, /")
      op = input()
b = float(input("Etrer nombre 2 : "))
print(f"{a} {op} {b} = {operation(a,b,op)}")"""


#Exercice C
notes = []


def moyenne(liste : list) -> float:
    """
    renvoie la moyenne des notes de la liste liste
    """
    total = 0
    for i in range(len(liste)):
        total += liste[i]
    return total/len(liste)

def minimum(liste : list) -> float:
    """
    Renvoie la plus petite note de la liste liste
    """
    minimum = 20
    for i in range(len(liste)):
        if (liste[i] < minimum):
            minimum = liste[i]
    return minimum

def maximum(liste : list):
    """
    Renvoie le maximum de la liste liste
    """
    maximum = 0
    for i in range(len(liste)):
        if (liste[i] > maximum):
            maximum = liste[i]
    return maximum


"""nb_notes = int(input("Combien de note voulez vous rentrer ? "))
if (nb_notes <= 0):
    raise ValueError("Le nombre de notes doit être strictement positif")

notes.clear()

for i in range(nb_notes):
    note_actuelle = float(input(f"Quelle est la note N°{i+1} "))
    while(note_actuelle > 20 or note_actuelle < 0):
        print("Incorrect la note doit être comrise entre 0 et 20 inclus")
        note_actuelle = float(input(f"Veuillez rentrer une note valide pour la note N°{i+1} "))
    notes.append(note_actuelle)
    
print(f"La moyenne des notes est : {moyenne(notes)}")
print(f"La note minimale est : {minimum(notes)}")
print(f"La note maximale est : {maximum(notes)}")"""



#Exercice D

for i in range(51):
    if (i%7 == 0):
        """print(f"{i} * 13 = {i*13}")"""
        
        
#Exercice E

def diviseurs(a : int) -> list:
    """
    Renvoie les diviseurs de a 
    """
    liste_div = []
    for i in range(1, a):
        if (a % i == 0):
            liste_div.append(i)
    return liste_div

def premier(a : int) -> bool:
    """
    Renvoie si a est premier
    """
    return (len(diviseurs(a)) == 1)



def somme(liste : list) -> float:
    """
    Renvoie la somme des termes d'une liste
    """
    total = 0
    for i in range(len(liste)):
        total += liste[i]
    return total

while True:
    a = int(input("Entrez un entier strictement positif "))
    div = diviseurs(a)
    chaine = ""
    for i in range(len(diviseurs(a))):
        chaine += str(diviseurs(a)[i]) + " " 
        
        
    if (a > 0):
        if (premier(a) == True):
            print(f"Diviseurs propres sans répétition de {a} : 1 donc Il est premier")
        else:
            print(f"Diviseurs propores sans répétition de {a} : {chaine} soit {len(div)} diviseurs propres dont la somme est  {somme(div)} ")
    else:
        raise ValueError("Le nombre doit être strictement positive")






        















        
    
    
    
    
    
    
    
    
    