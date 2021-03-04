ben={
    "mahendersing":14.5,
     "amitsheran":13.5,
     "rahul lal":13.0,
     "sandeep":12.5,
     "ankit":11.5,
     "aman":11.5,
     "vijay kumar":11.0,
     "snandal":11.0,
     "ajay":10.5,
     "ashish-kumar":14.5,
     "shrestha":11.5,
     "msehrawat":10.5,
     "pavan-kumar-sharavath":17.0,
     "rohit-kumar":16.0,
     "sumit-singh":13.5,
     "v.kumar":13.0,
     "l.mohar":11.5,
     "banty":11.5
     }
pune={
    "g.maruti":14.5,
     "s.singh":14.5,
     "Tajik":13.0,
     "s.shinde":13.0,
     "satpal":12.5,
     "yadav":12.5,
     "jadhav":12.5,
     "swanth":11.5,
     "manjeet":14.5,
     "skrishna":13.0,
    "sandeep":12.5,
    "amit":11.5,
    "pavan":15.5,
    "tomar":15.0,
    "kadian":14.0,
     "A.kumar":13.0,
     "sedaghat":12.5,
    "sriram":12.5,
    "sail":12.0,
    "pankaj":11.5
    }

borai=["pavan-kumar-sharavath","rohit-kumar","sumit-singh","v.kumar","l.mohar","banty","pavan", "tomar","kadian","A.kumar","sedaghat","sriram", "sail","pankaj"]
boall=["ashish-kumar","shrestha","msehrawat","manjeet","sandeep","skrishna","amit"]
bodef=[ "mahendersing","amitsheran","rahul lal","sandeep","ankit","aman","vijay kumar","snandal","ajay","swanth","jadhav","yadav","g.maruti","s.singh","Tajik","s.shinde","satpal"]
ra={}
rai={}
for pla in borai:
    if pla in ben:
        rai[pla]=ben.get(pla)    
    else:
        ra[pla]=pune.get(pla)    
raiders={**rai,**ra}

print("RAIDERS".center(40,"*"))
for r ,t in raiders.items():
    if r in rai:
        print(r,"-BEN-->",t,end="  cr.")
    else:
        print(r,"-PUN--->",t,end="  cr.")
    print()
alb={}
alp={}
for al in boall:
    if al in ben:
        alb[al]=ben.get(al)
    else:
        alp[al]=pune.get(al)
    print()
allround={**alb,**alp}
print("ALL-ROUNDERS".center(40,"*"))
for i,j in allround.items():
    if i in alb:
        print(i,"--BEN-->",j,end="  cr")
    else:
        print(i,"--PUNE-->",j,end="  cr")
    print()
bdeff={}
pdeff={}
for de in bodef:
    if de in ben:
        bdeff[de]=ben.get(de)
    else:
        pdeff[de]=pune.get(de)
    print()
defen={**bdeff,**pdeff}
print("DEFFENDERS".center(40,"*"))
for i,j in defen.items():
    if i in bdeff:
        print(i,"--BEN-->",j,end="  cr")
    else:
        print(i,"--PUNE-->",j,end="  cr")
    print()
while True:
    print("RAIDERS",raiders)
    print("ALLROUNDERS",allround)
    print("DEFENDERS",defen)
    print("you must enter only 7 players in the below from abouve players:")
    print('''Note:you must enter according to below rules:
                                ----->raiders between(1-3)
                                ----->deffenders between(1-4)
                                ----->allrounders between(1or 2)''')
    r=1
    a=1
    d=1
    total=100
    team={}
    for i in range(7):    
        play=input("enter your player:")
        if(i%7<=7):
            if (play in raiders)or(play in allround)or (play in defen): 
                if play in raiders:
                    if r<=4:
                        if play not in team:
                            team[play]=raiders.get(play)
                            x=raiders.get(play)                        
                            total=total-x                        
                            print("remaing point",total)
                            r=r+1
                    else:
                        print("sorry you have entered morethan  three raiders")
                        break
                elif play in allround:
                    if a<=3:
                        if play not in team:
                            team[play]=allround.get(play)
                            x=allround.get(play)
                            total=total-x
                            print("remaing points",total)
                            a+=1
                    else:
                        print('sorry you have entered morethan two(2) allrounders')
                        break
                elif play in defen:
                    if d<=2:
                        if play not in team:
                            team[play]=defen.get(play)
                            x=defen.get(play)
                            total=total-x
                            print("remaing points",total)
                            d+=1
                    else:
                        print("sorry you have enterd morethan 2 diffenders")
                        break
            else:
                print("sorry you have enterd not worng player")
                break
        if (total>=0):
            print("your team",team)
        else:
            print("sorry you dot not have points to buy this player")
            break
    new_team=input("IF DO YOU WANT TO CREATE ONE MORE TEAM place enter (yes) otherwise enter (no)")
    if (new_team=="no"):
        print("YOUR TEAM=",team)
        break
    else:
        continue


#print(team)

