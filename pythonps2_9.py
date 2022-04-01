def abs1(x):
    if (type(x) == "int" or type(x) == "float"):
        if (x>=0):
            return x
        elif ( x<=0):
            return -x
    else:
        r = x.real
        i = x.imag
        u = (r*r + i*i)**0.5
        return u

u = abs1(4)    
print(u)
