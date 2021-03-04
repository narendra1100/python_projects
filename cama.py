num=input("enter multiple with space number:")
spli=num.split()
'''ans=",".join(spli)
print(ans)
'''
tab=" "
count=0
for word in spli:
    count=count+1
    tab=tab+word
    if(count<len(spli)):
       tab=tab+"-"
print(tab)
