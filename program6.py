class Utilisateur:
    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0):
	    self.nom = nom
	    self.email = email
	    self.mot_de_passe = mot_de_passe
	    self.genre = genre
	    self.age = age

	    def display(self):
	        print self.nom, "\t", self.email, "\t", self.mot_de_passe, "\t", self.genre, "\t", self.age




class Module:

	    def __init__(self, nom="", volume_horaire=0, semestre=""):
	        self.nom = nom
	        self.volume_horaire = volume_horaire
	        self.semestre = semestre


	    def display(self):
	        print(self.nom, "\t", self.volume_horaire, "\t", self.semestre)




class Professeur(Utilisateur):

	    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0, ppr=0, grade=""):
	        super().__init__(self, nom, email, mot_de_passe, genre, age)
	        self.ppr = ppr
	        self.grade = grade


	    def display(self):
	        print(self.ppr, "\t", self.grade)




class Matiere:

	    def __init__(self, nom="", pourcentage=0):
	        self.__nom = nom
	        self.__pourcentage = pourcentage


	    def display(self):
	        print(self.__nom, "\t", self.__pourcentage)




class Annee_Academique:
	    def __init__(self, anne=""):
	        self.__anne = anne


	    def display(self):
	        print(self.__anne)




class Etudiant(Utilisateur):

	    def __init__(self, nom="", email="", mot_de_passe="", genre="", age=0, code_massar=""):
	        super().__init__(nom, email, mot_de_passe, genre, age)
	        self.code_massar = code_massar


	    def display(self):
	        print(self.code_massar)




class Evaluation:

	    def __init__(self, note=0):
	        self.note = note


	    def display(self):
	        print(self._note)

