import math

l1 = (3,0)
l2 = (0,4)

n = len(l1)
s=0
for i in range(n):
   s += math.pow((l1[i]-l2[i]),2)
   
s = math.sqrt(s)
print(s)
