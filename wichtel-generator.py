### Wichtel-Generator

### Mit diesem Wichtel-Generator sollen Menschen nach einer Nutzereingabe einen 
### zufälligen anderen Menschen ziehen, um diesen an Weihnachten zu beschenken.
### Danach wird eine E-Mail versendet, um die Person über den gezogenen Wichtel
### zu informieren
### Version 1.0

import random ### Bibliothek zur Auswahl einer Person
import datetime ### Nur für die Jahresangabe :)

anzahl_teilnehmer = int(input("Wieviele Teilnehmer gibt es?")) ### Festlegung der Teilnehmerzahl
print(f"In dieser Runde gibt es insgesamt {anzahl_teilnehmer} Wichtel.")

teilnehmer_schenker = [] ### Liste der Personen, welche ein Geschenk haben
teilnehmer_beschenkt = [] ### Identische Liste der Personen, welche ein Geschenk erhalten

### Schleife zur Erstellung der Teilnehmerliste

while anzahl_teilnehmer > 0:
    teilnehmer = input("Bitte gib deinen Vornamen ein!")
    teilnehmer_schenker.append(teilnehmer)
    teilnehmer_beschenkt.append(teilnehmer)
    anzahl_teilnehmer = anzahl_teilnehmer - 1

### Ausgabe der Listen zur Kontrolle 

print(teilnehmer_schenker)
print(teilnehmer_beschenkt)

### Ziehung der Wichtel

for name in teilnehmer_schenker:
    ziehung = random.choice(teilnehmer_beschenkt)
    teilnehmer_beschenkt.remove(ziehung)
    print(f"Hallo, {name}, du hast dieses Mal {ziehung} gezogen.")

### Ausschluss der Option den eigenen Namen zu ziehen

### Sendung der E-Mail an die Person "teilnehmer_schenker"

### Löschung der "Schenker"-Liste zur erneuten Verwendung des Programms

teilnehmer_schenker.clear()

### Abschluss des Programms

print(f"Frohe Weihnachten und ein schönes Neues Jahr!")

