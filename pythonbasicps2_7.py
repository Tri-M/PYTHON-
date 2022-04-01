A=[]
n=int(input("Enter nth number : "))
for i in range(0 ,n):
    e=int(input())
    A.append(e)
B=[]
n1=int(input("Enter nth number : "))
for i in range(0,n1):
    e1=int(input())
    B.append(e1)
def AtoB():
    for i in B:
        if i not in A:
            B1.append(i)
    print (B1)
def BtoA():
    for i in A:
        if i not in B:
            B2.append(i)
    print (B2)
B1=[]
B2=[]  
if (A == B) :
    print("Both the sets are same\n")
else:
    print("Sets are not same")
    print("Elements in B which are not in A as set B1:")
    AtoB()
    print("Elements in A which are not in B as set B2:")
    BtoA()