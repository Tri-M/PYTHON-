def runLengthEncode (plainText):
    res=''
    a=''
    for i in plainText:
        if a.count(i)>0:
            a+=i
        else:
            if len(a)>4:
                res+="/" + str(len(a)) + a[0][:1]
            else: 
                res+=a
                a=i
    return(res)
    
    
plainText="WWWBBBWWWBBBWWW"
runLengthEncode(plainText)