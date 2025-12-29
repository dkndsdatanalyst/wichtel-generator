### Wichtel-Generator

### Mit diesem Generatorprojekt soll eine Gruppe von Menschen eine Losung durchführen können, damit jeder
### eine Person erhält, welche er beschenken darf.

### Namenseingabe

anzahl_teilnehmer = int(input("Wieviele Teilnehmer gibt es?"))
int(anzahl_teilnehmer)
print(f"In dieser Runde gibt es insgesamt {anzahl_teilnehmer} Wichtel.")
teilnehmerliste = []

while anzahl_teilnehmer > 0:
    teilnehmer = input("Bitte gib deinen Vornamen ein!")
    teilnehmerliste.append(teilnehmer)
    anzahl_teilnehmer = anzahl_teilnehmer - 1

print(teilnehmerliste)


### Speicherung der Namen

### teilnehmerliste = []
### teilnehmerliste.append(teilnehmer)
### print(teilnehmerliste)

### Ziehung der Namen



### Ausschluss der Ziehung der gleichen Namen (jeder nur 1x)

### Anzahl der Ziehungen

### Entfernung des Namens aus dem Topf

### Automatische Sendung des Namens per E-Mail
