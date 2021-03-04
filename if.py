print("enter fristname and secondname below 10 charecter")
fristname=input("enter frist name:")
secondname=input("enter second name:")
if(fristname<=10 and secondname<=10):
    print("Hello ",fristname,secondname,"how are you")
    print("Hello "+fristname+" "+secondname+"how are you")
    print("Helllo{0} {1} how are you".format(fristname,secondname))
else:
    print("sorry you have enter above 10 charechter")
