#Funktionen (Unterprogramme, Subroutinein, Mehoden)

def begruessung():
    print("Schön dich zu sehen!")
    print("Viel Spaß mit dem Programm!")
    
print("Hallo Peter!")
begruessung()

def begruessungN4me(name):
    print("Hallo " + name + "!")
    print("Schön dich zu sehen!")
    print("Viel Spaß mit dem Programm!")
    
def begruessungN4men(*namen):
    for name in namen:
        print("Hallo " + name + "!")
        print("Schön dich zu sehen!")
        print("Viel Spaß mit dem Programm!")
        

    
print("Hallo Peter!")
begruessung()
begruessungN4me("Hansi")
begruessungN4men("Kevin", "Hanna", "Adi")

#Returns

def summe(a,b):
    return a + b

x = 4
y = 5
print("Summe aus ", x, "und ", y, "ist ",summe(x, y))
