def count(n):
    if n < 10 :
        return 1
    else :
        return 1 + count( n / 10 )

num = float(input("Enter a number :-"))
print("number of digit ",count(num))