
import os
import random
import shutil

if os.path.exists("../meals.txt"):
    with open("../meals.txt", "r+") as file:
        #lire le fichier
        meals_list = file.readlines()
        #choix aléatoire
        meals_random_choice = random.choice(meals_list)
        print(meals_random_choice)
        file.close()
else:
    print("le doc n'existe pas")


source = "../logo_test.png"
target = "../images/logo_test.png"

#copier coller un fichier
shutil.copy(source, target)

#Supression du fichier
os.remove(source)