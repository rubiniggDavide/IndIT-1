# importing the required module
import matplotlib.pyplot as plt

# array of every iteration-result
aLeibniz = []

#Assigning graph characteristics
plt.xlabel("Iteration")
plt.ylabel("Ergebnis der Leibniz-Reihe")
plt.title("Graph der Leibniz-Reihe")

iterations = int(input("Anzahl der Durchläufe angeben: "))
i = 0
counter = 0
while i < iterations:
    counter += (((-1)**i)/(2*i+1))
    i += 1

    aLeibniz.append(counter*4)
print(counter*4)

plt.plot(aLeibniz)
plt.show()