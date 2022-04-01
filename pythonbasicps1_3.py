digit=int(input("Enter how many times :"))
num=input("enter a number:")
 
 
result=0
for i in range(1,digit+1):
  result= result + int(str(num*i))
  print(num*i)
 
print("________________+\n")
print(result)
 