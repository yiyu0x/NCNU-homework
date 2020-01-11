import queue as q

class rev_pq:
	def __init__(self):
		self.q = q.PriorityQueue()

	def put(self, s):
		res = []
		for i in s:
			res.append(-ord(i))
		self.q.put(res)

	def get(self):
		res = ''
		for i in self.q.get():
			res += chr(-i)
		return res


q = rev_pq()
q.put('1')
q.put('2')
print(q.get())
print(q.get())

