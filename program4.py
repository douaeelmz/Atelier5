        #class Point avec la methode pour l'affichage du point sous forme de (x, y)
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def display(self):
        print "Le point : ", (self.x , self.y)

        #class Segment herite de la classe point avec la methode d'affichage
class Segment(Point):
    def __init__(self, x1, y1, x2, y2):
        self.orig = Point(x1,y1)
        self.extrem = Point(x2,y2)


    def display(self):
        print "L'origine est le point : ", (self.orig.x, self.orig.y), "L'extremite est le point : ", (self.extrem.x , self.extrem.y)

p1 = Point(1.2, 2.5)
p2 = Point()
p1.display()
p2.display()
seg1 = Segment(0, 0, 1.2, 2.5)
seg1.display()
# auto-test qui affiche une instance de Segment
if __name__ == '__main__':
        seg0 = Segment(1, 2, 3, 4)
        seg0.display()
