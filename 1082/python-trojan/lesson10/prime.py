def create_not_prime_number_pool(n):
    prime_list = [1]
    for i in range(2, n+1):
        if i not in prime_list:
            for j in range(i*i, n+1, i):
                prime_list.append(j)
    return prime_list

def get_prime(pool, n):
	for i in range(n+1):
		if i in pool:
			continue
		else:
			yield i

def main():
	n = eval(input("How many prime numbers do you want to get? "))
	pool = create_not_prime_number_pool(1000)
	gen = get_prime(pool, 1000)
	for i in range(n):
		print(next(gen))

main()