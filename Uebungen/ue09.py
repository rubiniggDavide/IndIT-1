# Dictionaries
woerterbuchDeutsch = {"Apfel": "apple",
               "Birne": "pear"}
woerterbuchEnglisch = {"apple": "Apfel",
               "pear": "Birne"}
try:
    begriff = input("Begriff: ")
    print(woerterbuchDeutsch[begriff]) # nur KeyError
except:
    try:
        print(woerterbuchEnglisch[begriff])
    except:
        print("Wort existiert nicht")
    
    

while True: # EIngabe bis Zahl eingegeben wurde
    try:
        stringA = input("Zahl: ")
        intb= int(stringA) # Umwanldung String to Int => nur ValueError möglich
        break
    except ValueError:
        print("ist keine Zahl")
print("ausgebrochen")