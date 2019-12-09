from rechteck import Rechteck
from kreis import Kreis
import random

class Formen:
    """
    Dient als Basis für die Klassen Rechteck und Kreis.
    """
    def __init__(self):
        return
    def flaeche(self):
        return
    def umfang(self):
        return
    def volumen (self, hoehe):
        print("Die Berechnung des Volumens ist noch nicht näher spezifiziert")

class Quader(Rechteck):
    """
    Klasse Quader zum Berechnen des Voluments eines Rechtecks.
    """
    def __init__(self, hoehe, breite, laenge):
        hoehe = 2
        self.hoehe = hoehe
        self.laenge = laenge
        self.breite = breite
    def volumen (self):
        return (self.hoehe * self.laenge * self.breite)

# Variablen

liste = []

quadrat = Rechteck(random.randint(1, 50), random.randint(1, 50))
rund = Kreis(random.randint(1, 50))

umfang_r = 0
umfang_k = 0

# Main

# Erstellen einer Liste mit 10 verschieden großen Rechtecken oder Kreisen

while len(liste) <= 9:
    quadrat = Rechteck(random.randint(1, 50), random.randint(1, 50))
    rund = Kreis(random.randint(1, 50))
    form = [quadrat, rund]
    liste.append(random.choice(form))


# Berechnen der Anzahl der Kreise in der Liste

count_r = sum(isinstance(x, Rechteck) for x in liste)
count_k = sum(isinstance(x, Kreis) for x in liste)


# Berechnen des Durchschnittlichen Umfangs der Kreise/Rechtecke in der erstellten Liste

for i in liste:
    if (type(i).__name__) == "Rechteck":
        rechteck = i
        umfang_r =+ (Rechteck.umfang(rechteck))
    if (type(i).__name__) == "Kreis":
        kreis = i
        umfang_k =+ (Kreis.umfang(kreis))


# Printausgabe

print("Anzahl der Rechtecke: {}".format(count_r))
print("Anzahl der Kreise: {}".format(count_k))
print("Durchschnittlicher Umfang eines Rechtecks: {}".format(umfang_r/count_r))
print("Durchschnittlicher Umfang eines Kreises: {}".format(umfang_k/count_k))


