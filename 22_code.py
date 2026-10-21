a=input("enter any string ")
b=""
for i in range(len(a)-1,-1,-1):
    b=b+a[i]
if a==b:
    print("the string is palindrome")
else:
    print("the string is not palindrome")