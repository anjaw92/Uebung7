
# coding: utf-8

# Spielerweiterung Try/Except
# Author: Anja Wallisch
# Datum: 09.12.2019

"""
Schere, Stein, Papier: Ein Spieler spielt gegen den Computer.
Sobald der Spieler oder der Computer 3 mal gewonnen haben, wird ein Gewinner gekürt und das Spiel beendet.
"""

# Imports
import numpy as np

#Variablen
zugelassen = ["schere", "stein", "papier"]
spieler_win = 0
pc_win = 0

#Main

while spieler_win < 3 and pc_win < 3:
    """
    Args:
        spieler1 (str): Input von Spieler 1
        pc (str): random choice aus Liste zugelassen
    Returns:
        win_pc + 1 wenn der Computer gewinnt
        win_spieler + 1 wenn der Spieler gewinnt
    Ends: wenn win_pc oder win_spieler den Wert 3 erreicht
    """
    try:
        print("Wähle zwischen Schere, Stein oder Papier")
        spieler = input("Spieler1: ")
        if spieler in zugelassen:
            pass
    except:
        print("Bitte wähle zwischen Schere, Stein oder Papier")

    pc = np.random.choice(zugelassen)
    print("Computer: " + pc)
    if spieler.lower() in zugelassen:
        if spieler.lower() == "schere":
            if pc == "schere":
                print("Unentschieden")
            elif pc == "stein":
                pc_win = pc_win + 1
                print("Der Computer hat gewonnen")
            elif pc == "papier":
                spieler_win = spieler_win +1
                print("Du hast gewonnen")
        if spieler.lower() == "stein":
            if pc == "stein":
                print("Unentschieden")
            elif pc == "papier":
                pc_win = pc_win + 1
                print("Der Computer hat gewonnen")
            elif pc == "schere":
                spieler_win = spieler_win + 1
                print("Du hast gewonnen")
        if spieler.lower() == "papier":
            if pc == "papier":
                print("Unentschieden")
            elif pc == "schere":
                pc_win = pc_win +1
                print("Der Computer hat gewonnen")
            elif pc == "stein":
                spieler_win = spieler_win +1
                print("Du hast gewonnen")
    else:
        print("Falsche Eingabe. Wähle zwischen Schere, Stein oder Papier")
else:
    if spieler_win == 3:
        print("Spieler 1 hat das Spiel gewonnen!")
    elif pc_win == 3:
        print("Du hast leider verloren. Versuche es doch noch einmal!")
    else:
        print("ERROR. Leider ist ein Fehler Aufgetreten. Bitte wiederhole das Spiel!")






