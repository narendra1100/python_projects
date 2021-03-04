print("WELCOME TO SEVEN HILLS BANK".center(100,"*"))
print("PLEACE INSERT YOUR 'ATM' CORD".center(50,"_"))
pasword=""
print("pleace enter you pasword here")
for i in range(4):    
    p=input()
    if len(p)==1:
        pasword=pasword+p
    else:
        print("sorry you must press enter again you enter a 'onedigite number'")
        break
if len(pasword)==4:
    print("ENQURY")
    print("WITH DRAW")
    print("TRANSFER")
    print("DEPOSIT")
    print('''note :
                            either you want to with draw
                            or you want to transfer
                            or you want to deposit
                            you must see the bank balence''')
    enqury=input("if you want to see balence you must enter like this BALENCE :")
    if enqury=="BALENCE" or "balence":
        import random
        amount=random.randint(1000,100000)
        print("your balence is =",amount)
        do=input('''if do you want to "with draw"or "transfer" or "deposit" .pleace enter (yes /no):''')
        if do =="yes"or "YES":
            print('''if do you want to
                                                    ----------->withdraw type like this:withdraw
                                                    ----------->transfer  type like this :transfer
                                                    ----------->deposit  type like this  :deposit   ''')
            choice=input("type here:")
            if (choice==("withdraw" or "WITHDRAW")):
                print("we have 50's,100's,200's,500's,2000's")
                print("you must maintain 1000 minimum balence")
                print("you must draw only 10000 rupees only for 1 transaction and  only you can with draw 100000 rupess for one week and you can withdraw only 4 times ")
                print("sir pleace enter aboue 1000 and below 29999")
                rupees=int(input("enter the amount:"))
                for  i in range(4):
                    if rupees>1000 and rupees <30000:
                        print("pleace collect your cash:",rupees)
                        amount=amount-rupees
                    con=input("do you want to continue  the transaction(yes/no):")
                    if con=="yes":
                        continue
                    else:
                        break
                print(amount)
            elif choice==("transfer" or "TRANSFER"):
                acc=input("pleace enter your 12 digit account no:")
                if len(acc)==12:
                    ph=input("pleace enter your 10 digit number:")
                    if len(ph)==10:
                        tacc=input("pleace enter your 12 digits of tracsfer account number:")
                        if len(tacc)==12:
                            rupes=int(input("enter your trasfer amout :"))
                            amount=amount-rupes
                            print("your remaing balence is:",amount)
            elif choice=="deposit":
                cas=int (input("enter how many rupees do you want to deposit:"))
                if cas>=500:
                    amount=amount+cas
                    print("now your amount is:",amount)
    
        
    else:
        print("ok thankyou")
print("THANK YOU")
                        
    
                                                    
