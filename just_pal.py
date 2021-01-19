n=int(input("enter the number :"))
u=n
s=0
while u>0:
    rem=u%10
    s=s*10+rem
    u//=10
if s==n:
    print("it is palindrom number")
else :
    print("not a palindrom number")
    
