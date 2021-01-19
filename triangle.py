##'''l=['a','b','c','d','e','f','g','h','i','j']
##num=int(input("enter any number"))
##for row in range(1,num):
##    for col in range(1,num-row):
##        print(" ",end="  ")
##    for col1 in range(row):
##        print("  ",l[col1],end=" ")
##    print()
##for row1 in range(1,num-1):
##    for col2 in range(1,row1):
##        print("  ",end=" ")
##    for col3 in range(num-row1-1):
##        print(" ",l[col3],"  ",end="")
##    print()'''
'''for row in range(1,8):
    for col in range(1,6):
        if(col==1) or( col==5 and(row!=0 and row!=4 and row!=7))or(( row==1 or row==4 or row==7)and(col>1 or col<5)):
            print("B",end="")
        else:
            print(end="    ")
    print()
for row in range(1,6):
    for col in range(1,6):
        if(col==1 and(row!=0 and row!=5 )) or(row==1 )or (row==5):
            print("HARI",end=" ")
        else:
            print(end="   ")
    print()'''
'''for row in range(1,6):
    for col in range(1,6):
        if(col==1 or col==5)or(row==1 or row==5):
            print("D",end=" ")
        else:
            print(end="     ")
    print()
for row in range(1,8):
    for col in range(1,6):
        if (col==1) or (row==1 or row==4 or row==7):
            print("E",end="")
        else:
            print(end="")
    print()'''



