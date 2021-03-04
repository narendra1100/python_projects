know_group=" "
while True:
     col_group=input("enter groups")#enter college group from the use
     list_=["BCOM","BA","BSC","BBM","BCA","BZC"]
     groups=False
     for group in list_:
         if(group==col_group):
             print("your group is available in my college",group)
             groups=True
             break
    if(not groups):
        print("your group is not available in my college")
know_group=input("do you want to continue know group(yes/no):")
if(know_group="no"):
        break
    else:
    continue

