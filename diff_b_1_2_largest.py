l = [5,10,8,1,7,9]
l1 = l[0]
for i in range (1,len(l)):
  if l1<= l[i]:
    l1 =l[i]
print(l1)
l2 =l[0]
for i in range(1,len(l)):
  if l1>l[i] and l2<l[i]:
    l2 =l[i]
print(l2)
n1 = l.index(l2)
n2 = l.index(l1)
d = 0
for i in range(min(n1,n2)+1,max(n1,n2)):
  d += l[i]
print(d)