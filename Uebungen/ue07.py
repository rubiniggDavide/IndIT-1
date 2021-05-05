#list.insert(index)

#list.append()

#list.remove(2)

liste1=[1,2,3]
liste2=[4,5,6]
gesamtliste = liste1 + liste2
print(gesamtliste)

vorname = "Joe"
nachname = "Mama"
name = vorname + " " + nachname
print("Name: " + name)

liste3 = ["ab", "cd", "ef"]
liste4 = 4 * liste3
print("Liste 3: ", liste3)
print("Liste 4: ", liste4)

liste3[0] = "z"
print("Liste 3: ", liste3)

liste5 = ["x", "y", "z"]
liste5 [2] = "a"
print(liste5)

#BSP zur Vervielfältigung von Litenalemente als Inhalt einer Gesamtliste (multiplikation)
liste6 = 4 * liste5
print(liste6)
#BSP zur Vervielfältigung von Listen als Unterlisten einer Gesamtliste (multiplikation)
liste6 = 4 * [liste5] #Verknüpfte Listen
print(liste6)
print(liste6[0][0])

#Änderung eines Zeichens einer Subliste führt zu Änderung der Kopien
liste6[0][0] = "p"
print(liste6)
liste5[0]= "x"
print(liste6)
