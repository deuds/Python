# l'épicerie est elle ouverte ?
# fonction avec en entrée une variable par défaut aléatoire pourvant etre forcée a une valeur fixe
from numpy.random import randint

def fonc_ouverture (heure_cour = randint (0,24)):
# Affichage de l'heure choisie
    print ("Il est actuellement ",heure_cour," heure")
# Définition des heures d'ouverture
    ouv_matin = 8
    ferm_matin = 12
    ouv_am = 14
    ferm_am = 18
# test epicerie ouverte 
    if ouv_matin < heure_cour < ferm_matin:
        return True
    elif ouv_am < heure_cour < ferm_am:
        return True
    else:
        return False