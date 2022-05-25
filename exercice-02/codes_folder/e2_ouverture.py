# l'épicerie est elle ouverte ?
# fonction avec en entrée une variable par défaut aléatoire pourvant etre forcée a une valeur fixe

# *********************************
# import de la bibliotheque numpy pour l'aléatoire a soortir de la fonction dans un deuxieme temps
from numpy.random import randint

def fonc_ouverture (heure_cour = randint (0,24),minute_cour = randint (0,60)):

# Affichage de l'heure choisie ou tirée au sort
    print ("Il est actuellement ",heure_cour," heure et ",minute_cour,"minutes")

# Définition des heures d'ouverture
    horaires = (8,12,14,18)
# convertion heure en minutes pour faciliter les tests
    hm_cour = (heure_cour*60+minute_cour)

# Affichage des horaires d'ouverture
    print ("MATIN :","\n ouverture : ",horaires[0],"\n fermeture : ",horaires[1])
    print ("APRES-MIDI :","\n ouverture : ",horaires[2],"\n fermeture : ",horaires[3])    

# test si l'épicerie ouverte 
    if (((hm_cour) >= (horaires[0]*60)) and ((hm_cour) <= (horaires[1]*60)) 
    or ((hm_cour) >= horaires[2]*60) and ((hm_cour) <= horaires[3]*60)):
        return True
    else:
        return False
