#Cree un compteur de voyelles

def get_vowels_number(word):
    #le compteur
    nb_vowels = 0

    #Pour chaque lettre du mot vous vérifier s'il s'agit d'une voyelle
    for letter in word:
        if letter in ['a','e','i','o','u']:
            #on ajoute 1 au compteur
            nb_vowels += 1
    #renvoyer le compteur
    return nb_vowels

word = input("Entrer un mot")
vowels_count = get_vowels_number(word)
print("Il y a ", vowels_count, "Voyelles dans le mot ", word)

