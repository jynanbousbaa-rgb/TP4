class Noeud: 
    def __init__(self, valeur, enfants=None):
        self.valeur = valeur
        self.enfants = enfants
        if self.enfants is None : self.enfants = []

    def ajouter_noeud(self, noeud):
        if not isinstance(noeud, Noeud):
            raise TypeError("Le type n'est pas un Noeud.")
        else :
            return self.liste.append(noeud)

    def affiche_exp(self):
        print(self.valeur, end=" ") 
        for noeud in self.enfants:
            noeud.affiche_exp()

n3 = Noeud(2, [])
n4 = Noeud("y", [])
n2 = Noeud("+", [n3, n4])
n1 = Noeud("exp", [n2])

n1.affiche_exp()






    # def affichage_expression(self, a):
    #     liste_enfants = []
    #     if not isinstance(a, Noeud):
    #         raise TypeError("Le type n'est pas un Noeud.")
    #     for enfant in a.enfants : 
    #         for petit_enfants in enfant.enfants :
    #             liste_enfants.append(petit_enfants)
    #         liste_enfants.append(enfant)
    #     liste_enfants.append(a)
    #     for i in liste_enfants[::-1]:
    #         print(i)
    #         print(" ")