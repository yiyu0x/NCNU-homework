import socket, sys

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

	def get_str(self):
		return f"{self.numerator}/{self.denominator}"

MAX_BYTES = 1024
def recv_something():
	data = sock.recv(MAX_BYTES)
	message = data.decode('UTF-8')
	print("Receiving:", message)
	return message

host = 'midterm.ncnu.net'
port = 1063

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect( (host, port) )

msg = recv_something()
target_arr = msg.split()

isFirst = True
for elemet in target_arr:
	if isFirst:
		result = Rational(int(elemet[0]), int(elemet[2]))
		isFirst = False
	elif elemet != '+':
		result.add(Rational(int(elemet[0]), int(elemet[2])))
		result.reduce()

msg = result.get_str().encode('UTF-8')
sock.send(msg)
recv_something()
sock.close()