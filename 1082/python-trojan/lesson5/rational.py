class Rational:
	
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator

	def __str__(self):
		return f"{self.numerator}/{self.denominator}"

	def add(self, b):
		self.numerator = self.numerator * b.denominator + b.numerator * self.denominator
		self.denominator = self.denominator * b.denominator
		return self

	def gcd(self, a, b):
		return a if b == 0 else self.gcd(b, a % b)

	def reduce(self):
		g = self.gcd(self.numerator, self.denominator)
		self.numerator //= g
		self.denominator //= g
		return self

	

def main():
    a = Rational(24, 36)
    print(a)
    a.reduce()
    print(a)
    b = Rational(2, 3)
    c = a.add(b)
    c.reduce()
    print(c)
main()