def e_o_sum(y):
    esum=0
    osum=0
    for i in y:
        if i%2==0:
            esum=esum+i
        else:
            osum=osum+i
    return (esum,osum)
def con(u):
    return tuple(u)
def mini(u):
    
    m=u[0]
    for num in u:
        if num<m:
            num=m
        
    return m
