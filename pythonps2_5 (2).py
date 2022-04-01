l=[1,2,3,4,5]
new_list=[]
min1 = min(l)
max1 = max(l)

for i in range(len(l)):
    new_list.append((l[i] - min1)/(max1 - min1))

print(new_list)

