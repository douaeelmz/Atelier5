class Etudiant:
    def __init__(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne

#creation et implementation du list

list = []
list.append(Etudiant('El Mziryahi', 'Douae', 19, "P132507453", 16.46))
list.append(Etudiant('Radi', 'Chifae', 21, "F133302974", 12))
list.append(Etudiant('Hani', 'sanae', 20, "I140457896", 15.14))
list.append(Etudiant('Sami', 'rayan', 22, "F133302974", 14))

#affiche les element du list

print "Nom ", "Prenom ", "Age ", "CNE ", "Moyenne\n"
for i in range(0, len(list)):
    print list[i].nom, list[i].prenom, list[i].age, list[i].cne, list[i].moyenne

#sort selon l'age


def sortByAge(Etudiant):
    return Etudiant.age


list.sort(key=sortByAge)

print "sort by age : \n "
for Etudiant in list:

    print Etudiant.nom, Etudiant.prenom, Etudiant.age



# sort selon la moyenne
def sortByAverage(Etudiant):
    return Etudiant.moyenne

list.sort(key=sortByAverage)

print "\nsort by Average : \n"
for Etudiant in list:
    print Etudiant.nom, Etudiant.prenom, Etudiant.moyenne


