def main():
	import multiprocessing
	slaves = ['Alice', 'Bob']
	q = multiprocessing.Queue()
	pList = []
	counter = 0
	for s in slaves:
		p = multiprocessing.Process(target=f, args=(s, q))
		p.start()
		pList.append(p)
		counter += 1
	# for p in pList:
		# p.join()
	print("="*20)
	# while not q.empty() and :
	# result = q.get()
	while counter:
		result = q.get()
		if result == '\x00':
			counter -= 1
		else:
			print( 'res:', result )
	print('end')

def f(name, q):
	import time, random
	n = random.randint(2, 10)
	for i in range(n):
		time.sleep( 0.1 * random.randint(1, 5) )
		msg = "{} - {}/{}".format(name, i+1, n)
		print("Inserting", msg)
		q.put(msg)
	q.put('\x00')

if __name__ == "__main__":
	main()