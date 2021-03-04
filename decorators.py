
r=[2,5,6,88,4,1]
g=r[0]
for i in r:
    if g<i:
        g=i
print(g)
'''
def num():
    return 7

def decorate(fun):
    def inner():
        a=fun+7
        return a
    return inner

f=decorate(num)
print(f)

def nari():
    for i in range(1,11):
        yield i
g=nari()
print("return values",next(g))
for i in g:
    print(i)
'''
