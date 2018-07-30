from math import pow

n = 1000

for a in range(1,n):
	for b in range(1,n):
		for c in range(1,n):
			d = (pow(a,3) + pow(b,3) - pow(c,3)) ** (1. / 3)
			d = round(d.real)
			if pow(a,3) + pow(b,3) == pow(c,3) + pow(d.real,3):
				print (a,b,c,d)