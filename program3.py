# creation du class rectanlge
class Rectangle:
    def __init__(self, longeur=4, largeur=2):
        self.longeur = longeur
        self.largeur = largeur
        self.nom = 'Rectangle'
#la methode qui calcule la surface du rectangle
    def surface(self):
        return self.longeur*self.largeur
#la methode qui affiche le nom est les parametres du rectangle
    def display(self):
        print (self.nom)
        print "Longeur :", self.longeur, "Largeur :", self.largeur, "Surface :", Rectangle.surface(self)

#creation du class carre qui herite du class rectangle
class Carre(Rectangle):
    def __init__(self, l=4):
        Rectangle.__init__(self)
        self.longeur = l
        self.largeur = l
        self.nom = "Carre"

#creation des objets
Rec = Rectangle(4,2)
Rec.display()
carr = Carre(5)
carr.display()
