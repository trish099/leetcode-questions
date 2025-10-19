# palindrome number
# brute force ie O(n)
x = 121
z = 0
k = x
while x>0:
  y = x%10
  z = z*10+y
  x = x//10
if k == z:
  print("True")
else:
  print("False")
# brute force O(n)
a = str(x)
h = ""
for i in range(len(a)-1,-1,-1):
  h += a[i]
if a == h:
  print("True")
else:
  print("False")
# more optimal solution ie O(1)
a = str(x)
print(a==a[::-1])


