"Napisz skrypt wyliczający wyznacznik macierzy wygenerowanej losowo"

from numpy import random
import numpy as np

def determinant():
    M = random.randint(5, size=(3,3))  #size=(kolumny, wiersze)
    print(M)
    determinant = np.linalg.det(M)
    print(determinant)

if __name__ == '__main__':
    determinant()
