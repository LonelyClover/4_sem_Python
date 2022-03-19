from fractions import Fraction

f = []
for i in range(3):
	args = input().split(' ')
	f.append(Fraction(int(args[0]), int(args[1])))

ans = f[1] / f[0] + f[1] / (f[0] + f[2]) - f[2] / (f[2] - f[0])
print(round(float(ans), 4))
