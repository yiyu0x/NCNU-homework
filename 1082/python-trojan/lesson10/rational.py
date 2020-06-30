def gcd(a, b):      # Greatest Common Divisor
    if b == 0: 
        return a
    else:
        return gcd(b, a % b)

class Rational:
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d
    def reduce(self):
        g = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // g
        self.denominator = self.denominator // g
    def __str__(self):
        self.reduce()
        return str(self.numerator) + '/' + str(self.denominator)
    
    def approximate(self):
        quotient = self.numerator // self.denominator
        reminder = self.numerator % self.denominator
        yield quotient
        yield '.'
        while True:
            yield (reminder * 10) // self.denominator
            reminder = (reminder * 10) % self.denominator

def print_value(r, d = 0):
    c = r.approximate()
    print( next(c), end='' )
    if d > 0:
        print( next(c), end='' )
        for i in range(d):
            print( next(c), end='' )
    print()

def main():
    a = Rational(1, 7)
    b = Rational(10, 3)
    c = Rational(10, 4)
    print_value(a, 7)
    print_value(a, 2)
    print_value(a, 300)
    print_value(b, 2)
    print_value(b)
    print_value(c, 3)
    print_value(c)

main()


