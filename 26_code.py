n=int(input("enter the number"))
copy=n
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
if rev==copy:
    print("number is pallidrome")
else:
    print("not pallidrome")

