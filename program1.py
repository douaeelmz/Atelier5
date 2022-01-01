#creation du class vecteur2D
class Vecteur2D:
    def __init__(self, x=0 , y=0):
        self.x = x
        self.y = y
    #la methode display
    def display(self):
        print (self.x , self.y)
#creation des objets du class vevteur2D
v1 = Vecteur2D()
v2 = Vecteur2D(2, 5)
print ("Le vecteur 1 :")
v1.display()
print ("Le vecteur 2 :")
v2.display()
