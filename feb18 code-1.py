def isprime(n):
	for i in range(2,n):
		if n%i==0:
			return False
	return True

n=int(input('enter the number : '))
c=0
for i in range(2,n+1):
	if isprime(i):
		print(i,end=' ')
		c=c+1
print(f'\n"{c}" is the total prime numbers in "{n}" natural numbers')