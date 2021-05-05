#liste = [1,2,4]
#print(liste)
#liste.insert(2,3)
#print(liste)
#liste.append(5)
#print(liste)
#liste.remove(4) #entfernt 4 nicht index 4
#print(liste)

#Erweitern Sie das Wörterbuch-BSP um die Möglichkeit Einträge zu ergänzen bzw zu löschen
woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_englisch = ["apple", "pear", "cerry", "melon", "apricot", "peach"]

def addWord(deutschesWort, englischesWort):
    woerterbuch_deutsch.append(deutschesWort)
    woerterbuch_englisch.append(englischesWort)
def searchWord(wordInput):
    index = 0
    for wort in woerterbuch_deutsch:  
        if wordInput.lower() == wort.lower():  
            break
        index +=1   
    
    if index == len(woerterbuch_deutsch):
        index=0
        for wort in woerterbuch_englisch:     
            if wordInput.lower() == wort.lower():
                break
            index +=1    
        
        if index == len(woerterbuch_englisch):
            print("Das Wort steht nicht im Wörterbuch")
            return -1
    return (woerterbuch_deutsch[index], woerterbuch_englisch[index], index)

addWord("Ananas", "pineapple")
addWord("Banane", "banana")
addWord("Drachenfrucht", "pitaya")

auswahl = "x"
while auswahl.lower != "q":
    auswahl = input("Befehl? \n[E]infügen \n[L]öschen \n[A]bfrage \n[Q]uit: ")
    if auswahl.lower() == "e":
        addWord(input("Deutsches Wort eingeben: "), input("Englisches Wort eingeben: "))
        
    elif auswahl.lower() == "l":
        output = searchWord(input("Welches Wort wollen Sie löschen?: "))
        if output != -1:
            woerterbuch_deutsch.remove(output[0])
            woerterbuch_englisch.remove(output[1])
    elif auswahl.lower() == "q":
        break
            
    else:
        output = searchWord(input("Zu übersetzendes Wort: "))
        if output != -1:
            print(output[0] + "[DE]")
            print(output[1]+ "[EN]")
    print(woerterbuch_deutsch)
    print(woerterbuch_englisch)
    
# ToDo: Trycatch for search function
# Anstelle von listen dictionaries verwenden.
# + ergänzung + löschen einbauen