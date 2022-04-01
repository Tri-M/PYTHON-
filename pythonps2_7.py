def check_sochastic(l):
    s=0
    for i in range(len(l)):
        s=0
        for j in range(len(l)):
            if(l[i][j]>=0):
                s+=l[i][j]
            else:
                return False
        if (s==1):
            continue
        else:
            return False

    return True




l=[[2,4,4],[4,8,8],[4,8,8]]
n = [[],[],[]]
for i in range(len(l)):
    for j in range(len(l)):
        n[j].append(l[i][j])


if (l==n):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")


if (check_sochastic(l)):
    print("The given matrix is a sochastic matrix")
else:
    print("The given matrix is not a sochastic matrix")


m=[[],[],[]]

for i in range(len(l)):
    for i in range(len(l)):
        



        
