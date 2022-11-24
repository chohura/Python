class kalkulator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b


a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
obj = kalkulator(a, b)
choice = 1
while choice != 0:
    print("0. Wyjdź")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    choice = int(input("Wybierz: "))
    if choice == 1:
        print("Wynik: ", obj.add())
    elif choice == 2:
        print("Wynik: ", obj.sub())
    elif choice == 3:
        print("Wynik: ", obj.mul())
    elif choice == 4:
        print("Wynik: ", round(obj.div(), 2))
    elif choice == 0:
        print("Wychodzenie")
    else:
        print("Podałeś złą cyfrę.")

print()
