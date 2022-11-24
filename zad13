'''Napisz skrypt realizujący mnożenie dwóch macierzy o rozmiarach 8x8'''

from numpy import random
import numpy as np

A = random.randint(5, size=(8,8))  #size=(kolumny, wiersze)
B = random.randint(5, size=(8,8))
C = np.zeros((8,8))

print("A = ",A)
print("B = ",B)


for i in range(len(A)):  #kolumny
    for j in range(len(B[0])):  #wiersze
        for k in range(len(B)):
            C[i][j] = C[i][j] + A[i][k] * B[k][j]



