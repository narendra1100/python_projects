d=[[3,4,5,6],[3,5,8,9]]
print(d)
g=[]
for i in range(len(d[0])):
    print("ivalue",i)
    print("d[0][i]",d[0][i],"d[1][i]",d[1][i])
    b=d[0][i]+d[1][i]
    print("bvalue",b)
    g.append(b)
    print("gvalue",g)
print(g)
'''
c=[]
for i in range(len(d[0])):
    print(i)
    b=d[0][i]-d[1][i]
    c.append(b)

print(c)
k=[]
for i in range(len(d[0])):
    b=d[0][i]*d[1][i]
    k.append(b)
print(k)
'''
