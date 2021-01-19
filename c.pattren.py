for row in range(1,6):
    for col in range(1,6):
        if (col==1 and row!=1) or (col==5 and row!=1) or(( row==1  or row==3)and(col!=1)) and (col>1 and col<5):
            print("0",end=" ")
        else:
            print("   ",end="")
    print()
for row_b in range(1,6):
    for col_b in range(1,6):
        if col_b==1   or( row_b==1 and col_b!=5) or (col_b==5 and row_b!=1) or  (row_b==3 and col_b!=5)  or (row_b==5 and col_b!=5) :
            print("b",end=" ")
        else:
            print("  ",end=" ")
    print()
for row_c in range(1,6):
    for col_c in range(1,6):
        if (col_c==1 and row_c!=1 and row_c!=5) or(( row_c==1 and col_c!=1) or (row_c==5 and col_c!=1)):
            print("C",end=" ")
        else:
            print("   ",end="")
    print()
for row_d in range(1,6):
    for col_d in range(1,6):
        if (row_d==1 and col_d!=5) or col_d==1 or (col_d==5 and row_d!=1) or row_d==5:
            print("D",end="")
        else:
            print("   ",end="")
    print()
for row_e in range(1,6):
    for col_e in range(1,6):
        if (row_e==1 or col_e==1 or row_e==5 or row_e==3):
            print("0",end="")
        else:
            print(" ",end="")
    print()
