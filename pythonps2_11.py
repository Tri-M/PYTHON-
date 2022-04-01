a = [3,6,9,12,15,21,24]

#assigning values to list c
n=len(a)
if (n%2==0):
    n1 = n//2-1
    n2 = n//2+1
else:
    n1 = n//2
    n2 = n//2+2
c = a[n1:n2]

#making new list b
b = list(a)

#deleting values from a
del a[n1]
del a[n1]


#Restoring values from c to a
a.insert(n1,c[0])
a.insert(n1+1,c[1])

