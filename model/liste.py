from random import shuffle

#générateur de pharse

#demander en console une chaine de la forme "mot1/mot2/mot3/mot4
chaine_word = input("Entrer une de la forme mot1/mot2/mot3/mot4")

#transformer cette chaine en liste
word = chaine_word.split("/")

#melanger la phrase
shuffle(word)

#récupérer le nombre d'éléments
word_len = len(word)

#si le nombre d'éléments de la liste est inférieur a 10
if word_len < 10:
    #afficher les 2 premier mots
    print(word[0], word[1])
    #ou print(word[0:1]
else:
    #afficher les 3 derniers
    print(word[2:3])
