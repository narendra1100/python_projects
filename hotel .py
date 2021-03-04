title="WELCOME TO MY HOTEL"

y=title.center(60,"*")
print(y)
items=["TEA","COFFE","ICE-CREAM","MEALS","IEDLI","PURI","AAMLATE"]
prices=["7","8","20","60","20","30","40"]
w="OUR MENU:"
print(w.center(20,"*"))
for i in range(len(items)):
    t=(items[i],"---------------------------------------------------------------------------------------------------------Rs.",prices[i])
    print(t)
cust_item=input("enter you item in aboue menu:")

