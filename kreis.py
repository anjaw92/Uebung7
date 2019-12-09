import math

class Kreis:
    """
    Klasse Kreis zum Berechnen der Fläche und des Umfangs eines Kreises.
    """
    def __init__(self, radius):
        self.radius = radius

    def flaeche(self):
        '''Berechnung der Fläche'''

        return(self.radius^2 * math.pi)

    def umfang(self):
        '''Berechnung des Umfangs'''

        return (2 * self.radius * math.pi)

