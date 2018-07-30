import math

n = 1000

for a in range(1,n):
	for b in range(1,n):
		for c in range(1,n):
			for d in range(1,n):
				if pow(a,3) + pow(b,3) == pow(c,3) + pow(d,3):
					print (a,b,c,d)
					break