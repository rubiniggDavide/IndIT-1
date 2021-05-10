#Slices
#slice[start:stop(:step)]

sequenz1 = "Ich bin ein Satz"

print(sequenz1[:3])
print(sequenz1[1:3])
print(sequenz1[0:7:2])
print(sequenz1[-2:])
print(sequenz1[-2::-1])
print(sequenz1[len(sequenz1)-3::-2])
sequenz2 = sequenz1.split()
print(sequenz2)

satz = sequenz1
for buchstabe in satz:
    print(buchstabe)
woerter = sequenz2
for wort in woerter:
    print(wort)
    
for i in range(0,9):
    print(i)
    
