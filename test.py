
def main():
    #recolte porte monnaie
    monnaie = int(input("Entrer valeur porte monnaie"))
    #creation du produits avec sa valeur
    product = int(input("Entrer valeur du produit"))
    #afficher la valeur du porte monnaie
    result = (product - monnaie)
    monnaie = result
    print("La valeur du porte monnaie est de " + str(monnaie))



if __name__ == '__main__':
    main()