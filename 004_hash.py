from math import pow

n = 1000

hashMap = {}

for c in range(1,1000):
	for d in range(1,1000):
		result = pow(c,3) + pow(d,3)
		hashMap[result] = [c,d]

for a in range(1,1000):
	for b in range(1,1000):
		result = pow(a,3) + pow(b,3)
		pair = hashMap.get(result)
		print(a,b,pair[0],pair[1])