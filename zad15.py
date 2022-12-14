'''Zdefiniuj klasę reprezentującą liczby zespolone (wraz z funkcjami na nich działającymi np. dodawanie, odejmowanie itp.)'''
class LiczbyZespolone(object):
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, no):
        self.re = self.re + no.re
        self.im = self.im + no.im
        return self

    def __mul__(self, o):
        return LiczbyZespolone(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def __str__(self):
        if self.im == 0:
            return '%.2f' % self.re
        if self.re == 0:
            return '%.2fi' % self.im
        if self.im < 0:
            return '%.2f - %.2fi' % (self.re, -self.im)
        else:
            return '%.2f + %.2fi' % (self.re, self.im)


def main():
   a = LiczbyZespolone(3, 5)
   b = LiczbyZespolone(4, 6)

   c = a + b

   print(c)

if __name__ == '__main__':
    main()
