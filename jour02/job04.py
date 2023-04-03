class Forme():    
    def aire(self):
        return 0
        
class Rectangle(Forme):
    def __init__(self):
        self.L = 10
        self.l = 5
    
    def aire(self):
        return (self.L * self.l)
    

F1 = Forme()
R1 = Rectangle()

print(R1.aire())