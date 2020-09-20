
#simulateur de ville

#création de class parent
class Batiment:
    def __init__(self, adresse,nb_etages):
        self.adresse = adresse
        self.nb_etage = nb_etages

    def get_adresse(self):
        return self.adresse

    def get_nb_etage(self):
        return self.nb_etage

#Creation classe immeuble
class Immeuble(Batiment):
    def __init__(self, adresse, nb_etage, nb_balcon):
        Batiment.__init__(self, adresse, nb_etage)
        self.nb_balcon = nb_balcon
        print("adresse: ", adresse, "etages: ", nb_etage, "balcons: ", nb_balcon)

    def get_nb_balcon(self):
        return self.nb_balcon


# Creation classe Supermarche
class Supermarche(Batiment):
    def __init__(self, adresse, nb_etage, nb_rayons):
        Batiment.__init__(self, adresse, nb_etage)
        self.nb_rayons = nb_rayons
        print("adresse: ", adresse, "etages: ", nb_etage, "rayons: ", nb_rayons)

    def get_nb_rayons(self):
        return self.nb_rayons

# Creation classe Banque
class Banque(Batiment):
    def __init__(self, adresse, nb_etage, nb_coffres):
        Batiment.__init__(self, adresse, nb_etage)
        self.nb_coffres = nb_coffres
        print("adresse: ", adresse, "etages: ", nb_etage, "coffres: ", nb_coffres,)

    def get_nb_coffres(self):
        return self.nb_coffres


#création d immeubles
immeuble1 = Immeuble("24 rue Jean mace", 3, 3)

#création Market
market = Supermarche("30 avenue Pierre roucin", 1, 12)

#création Bnaque
bank = Banque("10 rue rond point", 1, 3)

