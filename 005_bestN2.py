from math import pow

n = 1000

hashMap = {}

for c in range(1,1000):
	for d in range(1,1000):
		result = pow(c,3) + pow(d,3)
		hashMap[result] = [c,d]

for keys,values in hashMap.items():
    print(values[0],values[1],values[1],values[0])