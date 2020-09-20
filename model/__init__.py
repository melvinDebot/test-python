#transformer cette chaine en liste
word = chained_words.split("-")
print(word)

#la melanger
shuffle(word)

#récuperer le nombre d'elements
word_len = len(word)
print(word_len)

#si le nombre d'éléments de cette lsute est inférireur
if word_len < 10:
    print(word[0], word[1])
else:
    print(word[word_len -1], word[word_len -2], word[word_len -3],)