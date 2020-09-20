#juste prix
from random import randint

#choisir un nombre aléatoire entre 1 et 10
just_price = randint(1, 10)

#statue du jeu (activé, désactivé)
running = True

#tant que le jeu est en excécution
while running:
    #demander a l'utilisateur d'entrer un prix
    user_price = int(input("Entrer un prix"))

    #si le prix est le meme que le juste prix
    if user_price == just_price:
        print("Trouvé")
        #fin du jeu
    running = False

    #si le prix est supérieur
    if user_price > just_price:
        print("C'est moins")

    #si le prix est inférieur
    if user_price < just_price:
        print("C'est plus")

#fin du jeu
print("Fin de jeu")
