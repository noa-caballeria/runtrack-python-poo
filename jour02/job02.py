class Personne():
    def __init__(self):
        self.age = 14
    
    def afficher_age(self):
        print("La personne a ", self.get_age(), " ans.")
    
    def bonjour(self):
        print("Hello")
    
    def modifier_age(self, age):
        self.age = age
    

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
professeur1 = Professeur()

eleve1.modifier_age(15)
print(eleve1.age)
print(eleve1.bonjour()," ", eleve1.aller_en_cours())

professeur1.modifier_age(40)
print(professeur1.age)
print(professeur1.bonjour(), " ", professeur1.enseigner())