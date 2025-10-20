list1 = []
for i in range(len(s)):
  list1.append(s[i])
p1 = 0
p2 = len(list1)-1
while p1 < p2:
  if list1[p1] == "a" or list1[p1] == "e" or list1[p1] == "i" or list1[p1] == "o" or list1[p1] == "u" or list1[p1] == "A" or list1[p1] == "E" or list1[p1] == "I" or list1[p1] == "O" or list1[p1] == "U":
      if list1[p2] == "a" or list1[p2] == "e" or list1[p2] == "i" or list1[p2] == "o" or list1[p2] == "u" or list1[p2] == "A" or list1[p2] == "E" or list1[p2] == "I" or list1[p2] == "O" or list1[p2] == "U":
          list1[p2],list1[p1] = list1[p1],list1[p2]
          p1 +=1
          p2 -=1
      else:
          p2 -=1
  elif list1[p2] == "a" or list1[p2] == "e" or list1[p2] == "i" or list1[p2] == "o" or list1[p2] == "u" or list1[p2] == "A" or list1[p2] == "E" or list1[p2] == "I" or list1[p2] == "O" or list1[p2] == "U":
      p1 +=1
  else:
      p2 -=1
      p1 +=1
t = "".join(list1)
return t
