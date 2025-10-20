s = 0
p = 1
while n>0:
    y = n%10
    s = s+y
    p = p*y
    n = n//10
return p-s
