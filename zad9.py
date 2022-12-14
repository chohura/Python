'''Napisz skrypt obliczający pierwiastki równania kwadratowego
w postaci : y = ax2+bx+c. Wejściem skryptu są wartości: a, b, c'''

import math

a = int(input("Podaj wspolczynnik rowniania a: "))
b = int(input("Podaj wspolczynnik rowniania b: "))
c = int(input("Podaj wspolczynnik rowniania c: "))

delta = (b * b) - (4 * a * c)

print("delta = ", delta)

if delta > 0:
    x1 = -b - math.sqrt(delta) / (2 * a)
    x2 = -b + math.sqrt(delta) / (2 * a)

    print("x1 = ", x1)
    print("x2 = ", x2)

else:
    if delta == 0:
        x = -b / (2 * a)
        print("x = ", x)

    else:
        print("Równanie posiada brak miejsc zerowych")
