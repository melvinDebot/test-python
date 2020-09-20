
#Creation arme du joueeur
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def get_name(self):
        return self.name

    def get_damage_amount(self):
        return self.damage

#initialisation joueur
class Player:
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.healt = health
        self.attack = attack
        self.weapon = None
        print("Bienvenu au joueur", pseudo, health, attack)

    def get_pseudo(self):
        return self.pseudo

    def get_healt(self):
        return self.healt

    def get_attack(self):
        return self.attack

    def damage(self, damage):
        self.healt -= damage
        print("Aiie", damage)

    def attack_player(self,target_player):
        damage = self.attack

        #si le joueur a une arme
        if self.has_weapon():
            #ajoute les degats de l'arùe au point d'attaque du joueur
            damage += self.weapon.get_damage_amount()
        target_player.damage(damage)

    # methode pour changer d'arme
    def set_weapon(self, weapon):
        self.weapon = weapon

    #methode pour verifier si le joueeur a une arme
    def has_weapon(self):
        return self.weapon is not None



#SCENE
knife = Weapon("Couteau", 3)
player1 = Player("Melvin", 20, 3)

#donne un couteau faisant 3 de degats
player1.set_weapon(knife)
player2 = Player("Bob", 20, 5)

player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo())

print(player1.get_pseudo(), " Vie: ", player1.get_healt()," attaque: ", player1.get_attack())
print(player2.get_pseudo(), " Vie: ", player2.get_healt()," attaque: ", player2.get_attack())

