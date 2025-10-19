z= {}
list1 = []
for i in range(len(arr)):
  if arr[i] in z:
    z[arr[i]] = z[arr[i]]+1
  else:
    z[arr[i]] = 1
a = list(z.values())
for i in range(len(a)):
  if a[i] in list1:
    return False
  else:
      list1.append(a[i])
return True
# time complexity O(n+n) ie O(n)
