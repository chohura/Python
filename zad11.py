
def skalar():
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]
    #a = []
    #b = []
    list = []

    if len(a) == len(b):
        for i in range(len(a)):
            mnozenie = a[i] * b[i]
            list.append(mnozenie)
    else:
        print("bład")

    iloczyn_skalarny = sum(list)

    print(iloczyn_skalarny)
    return iloczyn_skalarny

if __name__ == '__main__':
    skalar()
