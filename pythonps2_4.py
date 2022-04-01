c, m = 0, 2
while c < 100 :
    for n in range(1, m) : 
        a = m * m - n * n 
        b = 2 * m * n 
        c = m * m + n * n 
        if c > 100 : 
            break
        print(a, "\t",b,"\t", c)
    m = m + 1
