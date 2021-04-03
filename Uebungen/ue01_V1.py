#Schreiben sie ein Programm, das
# 1) den Benutzer grüßt
# 2) eine erste Zahl entgegen nimmt
# 3) eine zweite Zahl entgegen nimmt
# 4) die add der beiden Zahlen berechnet und ausgibt
# 5) die diff der beiden Zahlen berechnet und ausgibt
# 6) das product der beiden Zahlen berechnet und ausgibt
# 7) den Quozien der beiden Zahlen berechnet und ausgibt (inkl. NAchkommastellen)

print("Servus")
number1 = float(input("Geben Sie die erste Zahl ein: "))
number2 = float(input("Geben Sie die erste Zahl ein: "))

def add(a, b):
    add = a + b
    print("Die Summe der beiden Zahlen lautet", add)

def diff(a, b):
    diff = a - b
    print("Die Differenz der beiden Zahlen lautet", diff)

def product(a, b):
    product = a * b
    print("Das Produkt der beiden Zahlen lautet", product)

def quotient(a, b):
    quotient = a / b
    print("Der Quotient der beiden Zahlen lautet", quotient)

add(number1, number2)
diff(number1, number2)
product(number1, number2)
quotient(number1, number2)

#Ungarische Notation verwenden:
#strZahl_1 = input("Erste Zahl: )
#intZahl_1 = int(strZahl_1)
#print(intZahl_1)
