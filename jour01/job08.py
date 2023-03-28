class Livre():
    def __init__(self):
        self.__autor = "Charles Baudelaire"
        self.__title = "Les Fleurs du Mal"
        self.__page = 404
        self.__available = True
    
    def set_title(self, title):
        self.__title = title
        return self.__title
    
    def get_title(self):
        return self.__title
    
    def set_autor(self, autor):
        self.__autor = autor
        return self.__autor
    
    def get_autor(self):
        return self.__autor
    
    def set_page(self, page):
        if page > 0:
            self.__page = page
            return self.__page
        else:
            print("Try an existing page.")
        
    def get_page(self):
        return self.__page
    
    def verify_available(self):
        if self.get_available():
            return True
        else:
            return False
                    
    def get_available(self):
        return self.__available

    def borrowed(self):
        if self.verify_available() == True:
            self.__available = False
                    
x = Livre()
print("The book ", x.get_title(), " writen by ", x.get_autor(), " is open at the page ", x.get_page())
x.set_autor("Jules Verne")
x.set_title("2 ans de Vacances")
x.set_page(0)
x.borrowed()
print(x.verify_available())
print("The book ", x.get_title(), " writen by ", x.get_autor(), " is open at the page ", x.get_page())
print("Is ", x.get_title(), "available ? \n", "\n", x.get_available())
print("The book ", x.get_title(), " writen by ", x.get_autor(), " is open at the page ", x.get_page())