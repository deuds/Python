# Combien il y a t il d'oeufs
# fonction definissant le nombre d'Oeufs de façon aléatoire avec possibilité de forcer la quantité
from numpy.random import randint
def fonc_nboeufs (nbr_oeufs = randint(0,24),nbr_lait = randint(0,24)):
    print("le stock d'oeufs est de : ",nbr_oeufs," oeufs")
    print("le stock d'oeufs est de : ",nbr_oeufs," oeufs")
    print('🥚'*nbr_oeufs)
    print("le stock de lait est de : ",nbr_lait," bouteilles")
    print('🍼'*nbr_lait)
    return(nbr_oeufs)
    return(nbr_lait)