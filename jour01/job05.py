class Animal():
    def __init__(self):
        self.years_old = 0
        self.name = "Luna"
    
    def set_age(self):
        self.years_old = self.years_old + 1
        return self.years_old
    def get_age(self):
        return self.years_old
    
    def animal_name(self, name):
        self.name = name
        print(self.name, "is the name of the Animal")
    
x = Animal()
print("The Animal have got ", x.get_age(), " year(s) old")
x.set_age()
print("The Animal have got ", x.get_age(), " year(s) old")
x.animal_name("Michel")