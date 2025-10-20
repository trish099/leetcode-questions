list1 = []
z = 0
for i in range(n):
    list1.append(start)
    start = start+2
for i in range(len(list1)):
    z = z^list1[i]
return z
