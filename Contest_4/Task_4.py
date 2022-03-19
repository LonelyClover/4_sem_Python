args = input().split(' ')

b = float(args[0])
q = float(args[1])
a = float(args[2])

n = 1

while b <= a:
	b *= q
	n += 1

print(n) 
