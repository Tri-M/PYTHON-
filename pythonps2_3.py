import math

l1 = (3,0,1)
l2 = (1,2,3)
s=0
for i in range(len(l1)):
    s += l1[i]*l2[i]


m1=0
m2=0
for i in range(len(l1)):
    m1 += l1[i]*l1[i]


for i in range(len(l2)):
    m2 += l2[i]*l2[i]

cos = s/(m1*m2)
eq=0
for i in range(len(l2)):
   eq += math.pow((l1[i]-l2[i]),2)
   



eq = math.sqrt(eq)
print("Cosine distance = ",cos)
print("Eucliden disctance = ",eq)
