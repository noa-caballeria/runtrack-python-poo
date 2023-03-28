class Personne():
    def __init__(self, firstname, name):
        self.name = name
        self.firstname = firstname
        
    def SePresenter(self):
        print(self.firstname, self.name)


personnes = [Personne("John","James"), Personne("Jane", "Doe"), Personne("John", "Doe"), Personne("Jane", "James")]

for i in personnes:
    i.SePresenter()