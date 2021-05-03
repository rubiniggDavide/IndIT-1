#Sequentielle Datentypen:

# 1) Strings / Zeichenketten
# => Objekte/Klasse
# ==> Methoden (Runktionen zur Manipulation von Klasseneigenschaften)
#

zeichenkette = "Ich bin ein String"
print(zeichenkette)
großbuchstaben = zeichenkette.upper()
print(großbuchstaben)
kleinbuchstaben = großbuchstaben.lower()
print(kleinbuchstaben)

buchstabe = zeichenkette[2]
print(buchstabe)
# Index von sequenziellen Elementen immer 0

# 2) Liste
meineListe = ["ich bin", "ein", "string in einer", "lsite"]
print(meineListe[2])
for woerter in meineListe:
    print(woerter)

woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
print(len(woerterbuch_deutsch))
woerterbuch_englisch = ["apple", "pear", "cerry", "melon", "apricot", "peach"]
def addWord(deutschesWort, englischesWort):
    woerterbuch_deutsch.append(deutschesWort)
    woerterbuch_englisch.append(englischesWort)
# 1 Eingabe Suchbegriff (deutsch->englisch)
# 2 Bestimmung der Gesamtanzahl der Elemente (= max Index)
# 3 Schleife: vergleich Eingabe mit Listenelement
# 4 Element gefunden? => Index speichern
# 5 Zugriff auf Listenelement[Index] im Englischen

addWord("Ananas", "pineapple")
addWord("Banane", "banana")
addWord("Drachenfrucht", "pitaya") 
wordInput = input("Zu übersetzendes Wort: ")
index = 0
for wort in woerterbuch_deutsch:
    
    if wordInput.lower() == wort.lower():
        print(woerterbuch_englisch[index])
        break
    index +=1
    
if index == len(woerterbuch_deutsch):
        print("Das Wort steht nicht im Wörterbuch")

print(woerterbuch_englisch[0][2])


listeVonListen = [["Apfel", "apple"], ["Birne", "pear"], ["Kirsche", "cerry"], ["Melone", "melon"]]
print(listeVonListen[1][1])

numberList = [[1, 2, 3], [4, 5, 6], [1, 2, 3]]


