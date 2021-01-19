num=int(input("how many list elements do want"))#it insert number into num
k=0
while (k<num):
    file=list([input("enter any sting")])
    x=[]
    i=0
    count=0
    while(i<=k):
        for y in range(0,i):
            count=count+1
            file.append(y[k])
        i=i+1
    k=k+1
print(x)
print(count)
