#!/usr/bin/env python

if __name__ == '__main__':
  osoba = input("Podaj imie, nazwisko i date urodzenia: ")
  [imie, nazwisko, data] = osoba.split(' ')
  print(imie)
  print(nazwisko)
  print(data)
