a = s.split(" ")
list1 = []
for i in a:
  t = i[::-1]
  list1.append(t)
k = " ".join(list1)
return k
