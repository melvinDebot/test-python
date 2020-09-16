
#systeme place cinéma

#recolter l'age de la personne
age = int(input("Quel age avez vous ?"))

#si la personne est mineur
if age < 18:
    price = 7
else:
    price = 12

#requete pop corn
pop_corn_request = input("Souhaitez-vous du pop corn ? (oui, non)")

#si oui
if pop_corn_request == "oui":
    price += 5
print("Vous devez payer ", price, " euros")




