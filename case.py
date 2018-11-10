from enum import IntEnum, unique
class Case:
    """
    Classe permettant de créer des objets de type case, composants élémentaires de la grille de jeu.
    """
    TAILLE = 10 # taille en pixels, le nom est en majuscules par convention, car c'est une constante
    def __init__(self, position, etat = Etat.vide, bateau = None):
        """
        :param position: position cartésienne de la case sur la grille
        :param etat: État de la case, lire la docstring de la classe "Etat" pour plus d'informations.
        :param bateau: AbstractBateau présent sur cette case. Si la case est vide, ce paramètre vaut "None"
        """
        self.position = list(position)
        self.etat = etat
        self._bateau = bateau


    def setBateau(self, bateau):
        """
        Mutateur de l'attribut "_bateau". Il sert à changer de bateau de manière sécurisée à condition qu'aucun coup n'ait été tiré.
        :param bateau: nouveau bateau
        :return: pas de sortie spécifiée
        """
        if bateau is not None:
            if self.etat == Etat.vide:
                self.etat = Etat.bateauInv
        else:
            if self.etat == Etat.bateauInv:
                self.etat = Etat.vide
        self._bateau = bateau


    def recevoirTir(self, ):
        if self._bateau is not None: # si un bateau est présent sur la case




@unique # Assure que chaque valeur de l'énumération est unique
class Etat(IntEnum):
    """
    Énumération décrivant les états possibles d'une case.
    "vide" veut dire que la case n'a rien de spécial.
    "bateauInv" veut dire qu'un bateau est présent, mais que la case est blanche
    "dansLEau" signifie que la case ne contient aucun bateau, mais qu'un coup a déjà été tiré dessus
    "touche" veut dire qu'un bateau a été touché sur cette case
    "coule" signifie qu'un bateau a été coulé ici
    "selectionne" veut dire que la case est en train d'être cliquée
    """

    vide = 0
    bateauInv = 1
    dansLEau = 2
    touche = 3
    coule = 4
    selectionne = 5