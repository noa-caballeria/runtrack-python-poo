class Livre():
    def __init__(self):
        self.__autor = "Charles Baudelaire"
        self.__title = "Les Fleurs du Mal"
        self.__page = 404
    
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
    
x = Livre()
print("The book ", x.get_title(), " writen by ", x.get_autor(), " is open at the page ", x.get_page())
x.set_autor("Jules Verne")
x.set_title("2 ans de Vacances")
x.set_page(16)
print("The book ", x.get_title(), " writen by ", x.get_autor(), " is open at the page ", x.get_page())
