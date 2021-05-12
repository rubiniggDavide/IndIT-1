#Schreiben sie ein Programm, das
# 1) den Benutzer grüßt
# 2) eine erste Zahl entgegen nimmt
# 3) eine zweite Zahl entgegen nimmt
# 4) die add der beiden Zahlen berechnet und ausgibt
# 5) die diff der kleineren von der Größeren
# 6) das product der beiden Zahlen berechnet und ausgibt
# 7) den Quozien kleinere Zahl durch größere Zahl  berechnet (inkl. NAchkommastellen)
print("Servus")
number1 = float(input("Geben Sie die erste Zahl ein: "))
number2 = float(input("Geben Sie die erste Zahl ein: "))

#number1 wird zur kleineren
if(number1 > number2):
    storedNumber = number2
    number2 = number1
    number1 = storedNumber
   
def add(a, b):
    add = a + b
    print("Die Summe der beiden Zahlen lautet", add)

def diff(a, b):
    """Zieht a von b ab"""
    diff = b - a
    print("Die Differenz der beiden Zahlen lautet", diff)

def product(a, b):
    product = a * b
    print("Das Produkt der beiden Zahlen lautet", product)

def quotient(a, b):
    """rechnet a durch b"""
    quotient = a / b
    print("Der Quotient der beiden Zahlen lautet", quotient)

add(number1, number2)
diff(number1, number2)
product(number1, number2)
quotient(number1, number2)

#if type(x) is int: