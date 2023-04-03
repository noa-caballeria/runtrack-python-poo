class Personne():
    def __init__(self):
        self.age = 14
    
    def afficher_age(self):
        print("La personne a ", self.get_age(), " ans.")
    
    def bonjour(self):
        print("Hello")
    
    def modifier_age(self, age):
        if self.age > 0:
            self.age = age
        else:
            print("Try a valid age.")
    

class Eleve(Personne):
    def aller_en_cours(self):
        print("Je vais en cours.")
    
    def affichage_age(self):
        print("Age :", self.age)
    
    
class Professeur(Personne):
    def __init__(self):
        self.__matiereEnseignée = "Physique-Chimie"
    
    def enseigner(self):
        print("Le cours va commencer")
    
    
personne1 = Personne()
eleve1 = Eleve()
eleve1.affichage_age()