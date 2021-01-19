while True:
    num_1=int (input("enter frist number:"))
    num_2=int(input("enter second number:"))
    list1=[]
    for number in range(1,num_1+1):
        if(num_1%number==0):
            list1.append(number)
    #print(list1)
    list2=[]
    for numb in range(1,num_2+1):
        if(num_2%numb==0):
            list2.append(numb)
    #print(list2)
    two=[]
    for k in list1:
        if k in list2:        
            two.append(k)
    print("the (GCD)of two numbers :",max(two))
    #max(two)
    close=input("do you know more(yes/no):")
    if(close=="no"):
        break
    else:
        continue
    
