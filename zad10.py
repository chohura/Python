'''Napisz skrypt sortujący liczby malejąco.
Wygeneruj losowo 50 liczb - wykorzystąj standardową funkcje do losowania.
Z wbudowanej funkcji sortującej korzystaj tylko w celu weryfikacji wyników'''

from random import randint

def generuj(n, od, do):
    """ Funkcja zwraca tablice majaca n elementow
    o losowych wartosciach z zakresu (od, do)"""
    tab = []
    while n > 0:
        tab.append(randint(od, do))
        n = n - 1
    return tab

def bubble(A):
  n = len(A)
  while n > 1:
    for i in range(0, n-1):
      if A[i] < A[i+1]:
        A[i], A[i+1] = A[i+1], A[i]
    n = n - 1
    print(A)

  return A

bubble(generuj(50,1,20000))
