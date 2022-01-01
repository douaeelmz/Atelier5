
class Vecteur2D:
    def __init__(self, x=0 , y=0):
        self.x = x
        self.y = y
    def display(self):
        print (self.x , self.y)
#la methode addition pour sommer deux vecteurs
    def Addition(self):
        a = int(input("valeur de x \t"))
        b = int(input("valeur de y \t"))
        v0 = Vecteur2D(a,b)
        print ((v0.x + self.x , v0.y + self.y))
#creation des objets du class vecteur2D

v1 = Vecteur2D()
v2 = Vecteur2D(2, 5)
print ("Le vecteur 1 :")
v1.display()
print ("Le vecteur 2 :")
v2.display()
print ("L'addition : ")
v2.Addition()
