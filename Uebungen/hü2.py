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
        print(woerterbuch_englisch[index]+ "[EN]")
        break
    index +=1
    
if index == len(woerterbuch_deutsch):
    index=0
    for wort in woerterbuch_englisch:
        
        if wordInput.lower() == wort.lower():
            print(woerterbuch_deutsch[index] + "[DE]")
            break
        index +=1    
    if index == len(woerterbuch_englisch):
        print("Das Wort steht nicht im Wörterbuch")

