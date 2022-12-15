'''Napisz program proszący użytkownika o dane zawierające kilka pól (może to być np. lista zadań z opisem
i terminami wykonania czy baza recenzji filmów) i zapisujący podane dane do pliku
w wybranym formacie (CSV/JSON). Przy każdym uruchomieniu program powinien odczytywać i wyświetlać wprowadzone
wcześniej dane, umożliwiać ich usunięcie (po jednym wpisie)
oraz dodanie nowych rekordów.'''

import json


class lektury():

    def __init__(self, name):
        self.name = name
        self.dane = ""

    def zapisz(self):
        with open(self.name, 'w', encoding="UTF-8") as plik:
            json.dump(self.dane, plik, ensure_ascii=False, indent=2)

    def odczytaj(self):
        with open(self.name, 'r', encoding="UTF-8") as plik:
            text = plik.read()
        self.dane = json.loads(text)

    def dodaj(self):
        tytul = input("Podaj tytuł: \n")
        autor = input("Podaj autora: \n")
        data = input("Podaj pierwsza date wydania: \n")
        gatunek = input("Podaj gatunek: \n")

        self.dane[tytul] = {'autor': autor,
                            'data': data,
                            'gatunek': gatunek}
        return self.dane


    def usun(self):
        tytul = input("Podaj tytuł do usunięcia: \n")
        del self.dane[tytul]

    def wyswietl(self):
        json_string = json.dumps(self.dane, ensure_ascii=False, indent=2).encode("UTF-8")
        print(json_string.decode())

    def program(self):
        self.odczytaj()
        self.wyswietl()
        i = input("Czy chcesz dodać nowe lektury? Y/N")
        if i == "Y":
            self.dodaj()
            i = input("Czy chcesz usunąć lektury? Y/N")
            if i == "Y":
                self.usun()
        else:
            i = input("Czy chcesz usunąć lektury? Y/N")
            if i == "Y":
                self.usun()
        self.zapisz()


def main():
    x = lektury('lektury.json')
    x.program()


if __name__ == '__main__':
    main()