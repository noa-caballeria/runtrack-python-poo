class Rectangle():
    def __init__(self):
        self.__L = 10
        self.__l = 5
        
    def perimetre(self):
        print((self.__L * 2) + (self.__l * 2))
        
    def surface(self):
        print(self.__L * self.__l)
        
    def set_L(self, L):
        self.__L = L
        return self.__L
    
    def get_L(self):
        return self.__L
    
    def set_l(self, l):
        self.__l = l
        return self.__l
    
    def get_l(self):
        return self.__l
    
    
class Parallelepipede(Rectangle):
    def __init__(self, L, l, h):
        self.L = L
        self.l = l
        self.h = h 
        
    def volume(self):
        print(self.L * self.l * self.h)
        
    
    
rectangle1 = Rectangle()
parallelepipede1 = Parallelepipede(10, 5, 2)

rectangle1.perimetre()
parallelepipede1.volume()