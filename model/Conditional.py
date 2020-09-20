#place de cinéma

#recolter l'age de la personne
age = int(input("Quel est votre age ?"))

#si l'age est mineur -> 7euro
if age < 18:
    prix_total = 7
#si la personne est majeur
else:
    prix_total = 12

#ou alors en ternaire
# prix_total = (7,12)[age < 18]

#souhaitez vous du pop corn
pop_corn_request = input("Souhaitez vous du pop corn  (oui, non) ?")

#si oui
if pop_corn_request == "oui":
    prix_total += 5

print("Vous devez payer ", prix_total, "euros")
