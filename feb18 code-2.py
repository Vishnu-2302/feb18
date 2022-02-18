n=int(input('enter the number : '))
f=1
c=0
d=0
for i in range(1,n+1):
	d=f*i
	print(f'{f} * {i} = {d} +')
	f=d
	c=c+d
print(f'= {c} is total value')
