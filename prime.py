while True:#eloop manam malli enkoka numberu primenumbera kada ani telusokovadanili upayogapadutundi
    num=int(input("enter number:"))#e line manam echhina numberu variable loki store cheyadaniki
    check=True#manam mundugane echhina number prime ani anumkuntam
    for number in (2,int(num/2+1)):#edi for loop endulo numberu 2 nika modalayi (number-1) varaku tirugutundi
        if(num%number==0):#loop loki vachhina taruvata manam echhina numberu loop lo unna number to divisiable aete e if condition work avvutundi
            check=False
            break
        else:#lekunte else statement work avvutundi
            check=True
    if check==False:#e line manam echhina for loop lo if statement corect aete e statement work avvutundi lekunte else statement work avvr tundi
        print("not prime")
    else:
        print("prime")
