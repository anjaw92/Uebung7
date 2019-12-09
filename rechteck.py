class Rechteck:
    """
    Klasse Rechteckt zum Berechnen von Fläche und Umfang
    """
    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite

    def flaeche(self):
        '''Berechneung der Fläche'''

        return(self.laenge * self.breite)

    def umfang(self):
        '''Berechnung des Umfangs'''

        return (2 * (self.laenge + self.breite))






