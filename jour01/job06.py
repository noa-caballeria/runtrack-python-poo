class Rectangle():
    def __init__(self):
        self.__L = 4
        self.__l = 12
        
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
    
x = Rectangle()
print("The Rectangle have for height ", x.get_L(), ", and ", x.get_l(), " for width") 
x.set_L(10)
x.set_l(5)
print("The Rectangle have for height ", x.get_L(), ", and ", x.get_l(), " for width") 