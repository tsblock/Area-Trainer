#Area Trainer is for students to practise calculating the areas of triangles, rectangles and circles, great for examination revision.
print("\nStarting programme...\n\n. . .")
import random,math,time,datetime,os,json
filename="users.json"
user=0
#Gets directory and verifies file location.
dirr=os.getcwd()
os.chdir(dirr)
#Login function where user first enters a username. If the username is in "users.json", it will tell the user to enter the password to that account.
def signup():
    time.sleep(1)
    with open("users.json","r")as f:
        users=json.load(f)
    updatedata(users)
    with open("users.json","w")as f:
        json.dump(users,f,sort_keys=True,indent=1)
#The function which updates the data that will be stored in the "users.json" file.
def updatedata(users):
    global user
    try:
        user=str(input("\nEnter a username: "))
        if not user in users:
            print("\nUsername not in database. Creating new account...")
            time.sleep(1)
            pas=str(input("\nEnter a password: "))
            users[user]={}
            users[user]["password"]=pas
            users[user]["score"]=0
            return user
        else:
            with open("users.json","r")as f:
                data=json.load(f)[user]
                print("\nUsername in database. Fetching info...")
                time.sleep(1)
                pas=str(input("\nEnter your password: "))
                fetch=users[user]["password"]
                while(pas!=fetch):
                    pas=str(input("\nIncorrect password. Please try again: "))
                print("\nLogin successful.")
                return user
    except:
        print("\n[ERROR] Unknown error.")
        signup()
#Calls the login function when the user runs the code.
signup()
#When the user chooses "Exit Programme" from the main menu, this function will be called.
def exitcont():
    global user,total
    print("\n================================\nYou have chosen: Exit Programme.\n================================")
    print("\nAre you sure you want to exit?\n\nEnter 1 to exit, or enter any other number to go back to main menu.")
    choic=3
    while(choic==3):
        try:
            choic=int(input("\nEnter a number: "))
            if(choic==1):
                with open("users.json","r")as f:
                    users=json.load(f)
                varr=addtotal(users)
                with open("users.json","w")as f:
                    json.dump(users,f,sort_keys=True,indent=1)
                print("\n. . .\n\nThank you for playing Area Trainer. See you next time.\n\nExiting in 3 seconds.\n\n.")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("\nStopping programme...\n")
                exit()
                return choic
            else:
                print("\nGoing back to main menu...")
                start()
        except ValueError:
            print("\n[ERROR] Invalid character(s).")
#Adds up the total points and saves it to "users.json" when the user decides to exit.
def addtotal(users):
    global user,total
    with open("users.json","r")as f:
        users[user]["score"]=total
    return users
#Function "x", the main menu.
def x():
    print("\n-----\n")
    if(nowday=="25")and(nowmonth=="12"):
        print("Ho ho ho. Merry Christmas.")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="29")and(nowmonth=="02"):
        print("Happy Leap Day.")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="01")and(nowmonth=="04"):
        print("We are sorry, the code is not working today.")
        time.sleep(2)
        print("Nah just kidding. Happy April Fools.")
        time.sleep(1)
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="01")and(nowmonth=="01"):
        print("Happy New Year. How was {}? We wish you all the best for {}. What are your New Year's resolutions?".format(year0,year1))
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="31")and(nowmonth=="10"):
        print("Boo. Happy Halloween.")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="04")and(nowmonth=="07"):
        print("Happy Independence Day.")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="04")and(nowmonth=="05"):
        print("Happy Star Wars Day. May the Fourth be with you.")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="01")and(nowmonth=="05"):
        print("Happy Labour Day.")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="26")and(nowmonth=="12"):
        print("Happy Boxing Day. What presents did you get for Christmas?")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="14")and(nowmonth=="03"):
        print("Happy Pi Day.")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="13")and(weekday=="5"):
        print("Happy Friday the Thirteenth.")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="20")and(nowmonth=="04"):
        print("Happy Weed Day. 420 blaze it.")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="11")and(nowmonth=="09"):
        print("Never forget.")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="31")and(nowmonth=="12"):
        print("Happy New Year's Eve. Are you excited for {}?".format(year2))
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="10")and(nowmonth=="10"):
        print("Happy World Mental Health Day.\nTo anyone suffering from mental illness, you are awesome, and you should never, ever give up.")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="11")and(nowmonth=="11"):
        print("Happy Veterans Day.")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="01")and(nowmonth=="10"):
        print("Happy International Coffee Day. Why not get yourself a nice cup of coffee?")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="03")and(nowmonth=="01"):
        print("Happy Bitcoin Genesis Day.\nOn this day in 2009, Satoshi Nakamoto mined the first Bitcoin block known as the genesis block.")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    elif(nowday=="01")and(nowmonth=="02"):
        print("Hello. Are you enjoying {} so far?".format(year1))
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    else:
        print("Hello.")
        if(total==1):
            print("\nYou have 1 point.")
        else:
            print("\nYou have {} points.".format(total))
    print(time.strftime("\nCurrent Time and Date: %c\n\n-----\n\nPlease do not force quit the programme or your score will not be saved.\n\nPlease select an option:\n\n1: Rectangle Area\n2: Triangle Area\n3: Circle Area\n4: About\n5: Guessing Game\n6: Exit Programme"))
    try:
        a=int(input("\nEnter a number from above: "))
        return a
    except:
        print("\n[ERROR] Invalid character(s).")
#When the user chooses either option 1, 2, or 3, this function will be called.
def area(choice):
    global total
    c=random.randint(1,101)
    d=random.randint(1,101)
    asdf=random.randint(1,51)
    big=random.randint(51,101)
    small=random.randint(1,50)
    pie=math.pi
    count=0
    #When the user chooses "Rectangle" from the main menu.
    if(choice==1):
        print("\n================================\nYou have chosen: Rectangle Area.\n================================")
        print("\nPlease select question type:\n\n1: Short Answer\n2: Multiple Choice\nAny other number: Back to Main Menu")
        try:
            samc=int(input("\nEnter a number from above: "))
            if(samc==1):
                print("\nGenerating question...")
                print("\n.")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                score=5
                e=int(input("\nWhat is the area of a rectangle with length {} and width {}? You have 5 tries. Answer: ".format(c,d)))
                ting=c*d
                while(e!=ting):
                    count+=1
                    score-=1
                    if(count==5):
                        e=ting
                        print("\nThe correct answer is {}. Going back to main menu...\n\n.".format(ting))
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return e
                    else:
                        e=int(input("\n[ERROR] Wrong answer. Please try again: "))
                total+=score
                if(score==1):
                    print("\nCorrect answer. You have gained {} point. Going back to main menu...\n\n.".format(score))
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("\n================================\nWelcome to Area Trainer.\n================================")
                else:
                    print("\nCorrect answer. You have gained {} points. Going back to main menu...\n\n.".format(score))
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("\n================================\nWelcome to Area Trainer.\n================================")
            elif(samc==2):
                lolrandom=random.randint(1,4)
                print("\nGenerating question...\n\n.")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                if(lolrandom==3):
                    print("\nWhat is the area of a rectangle with length {} and width {}? You have 1 try.".format(c,d))
                    ting=c*d
                    print("\n1:",random.randint(500,3000))
                    print("2:",random.randint(500,3000))
                    print("3:",ting)
                    print("4:",random.randint(500,3000))
                    again=int(input("\nEnter a number from above: "))
                    if(again==3)or(again==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        again=3
                        print("\nThe correct answer is 3. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return again
                elif(lolrandom==1):
                    print("\nWhat is the area of a rectangle with length {} and width {}? You have 1 try.".format(c,d))
                    ting=c*d
                    print("\n1:",ting)
                    print("2:",random.randint(500,3000))
                    print("3:",random.randint(500,3000))
                    print("4:",random.randint(500,3000))
                    againn=int(input("\nEnter a number from above: "))
                    if(againn==1)or(againn==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        againn=1
                        print("\nThe correct answer is 1. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return againn
                elif(lolrandom==2):
                    print("\nWhat is the area of a rectangle with length {} and width {}? You have 1 try.".format(c,d))
                    ting=c*d
                    print("\n1:",random.randint(500,3000))
                    print("2:",ting)
                    print("3:",random.randint(500,3000))
                    print("4:",random.randint(500,3000))
                    agai=int(input("\nEnter a number from above: "))
                    if(agai==2)or(agai==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        agai=2
                        print("\nThe correct answer is 2. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return agai
                else:
                    print("\nWhat is the area of a rectangle with length {} and width {}? You have 1 try.".format(c,d))
                    ting=c*d
                    print("\n1:",random.randint(500,3000))
                    print("2:",random.randint(500,3000))
                    print("3:",random.randint(500,3000))
                    print("4:",ting)
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==4)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=4
                        print("\nThe correct answer is 4. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
            else:
                print("\nGoing back to main menu...")
        except:
            print("\n[ERROR] An error occured.\n\nGoing back to main menu...\n\n.")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("\n================================\nWelcome to Area Trainer.\n================================")
    #When the user chooses "Triangle" from the main menu.
    elif(choice==2):
        print("\n================================\nYou have chosen: Triangle Area.\n================================")
        print("\nPlease select question type:\n\n1: Short Answer\n2: Multiple Choice\nAny other number: Back to Main Menu")
        try:
            succ=int(input("\nEnter a number from above: "))
            if(succ==1):
                lol=random.randint(1,5)
                print("\nGenerating question...\n\n.")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                if(lol==3):
                    score=5
                    fdsa=float(input("\nWhat is the area of a triangle with base {} and hypotenuse {}? You have 5 tries. Answer (2 decimal places): ".format(small,big)))
                    ans=round(float((1/2*small)*math.sqrt((big**2)-(small**2))),2)
                    while(float(fdsa!=ans)):
                        count+=1
                        score-=1
                        if(count!=5):
                            fdsa=float(input("\n[ERROR] Wrong answer. Please try again: "))
                        else:
                            fdsa=ans
                            print("\nThe correct answer is {}. Going back to main menu...\n\n.".format(ans))
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("\n================================\nWelcome to Area Trainer.\n================================")
                            return fdsa
                    total+=score
                    if(score==1):
                        print("\nCorrect answer. You have gained {} point. Going back to main menu...\n\n.".format(score))
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        print("\nCorrect answer. You have gained {} points. Going back to main menu...\n\n.".format(score))
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                elif(lol==5):
                    score=5
                    qw=float(input("\nWhat is the area of a triangle with height {} and hypotenuse {}? You have 5 tries. Answer (2 decimal places): ".format(small,big)))
                    asw=round(float((1/2*small)*math.sqrt((big**2)-(small**2))),2)
                    while(float(qw!=asw)):
                        count+=1
                        score-=1
                        if(count!=5):
                            qw=float(input("\n[ERROR] Wrong answer. Please try again: "))
                        else:
                            qw=asw
                            print("\nThe correct answer is {}. Going back to main menu...\n\n.".format(asw))
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("\n================================\nWelcome to Area Trainer.\n================================")
                            return qw
                    total+=score
                    if(score==1):
                        print("\nCorrect answer. You have gained {} point. Going back to main menu...\n\n.".format(score))
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        print("\nCorrect answer. You have gained {} points. Going back to main menu...\n\n.".format(score))
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                else:
                    score=5
                    f=float(input("\nWhat is the area of a triangle with base {} and height {}? You have 5 tries. Answer: ".format(c,d)))
                    ol=float(c*d/2)
                    while(float(f!=ol)):
                        count+=1
                        score-=1
                        if(count!=5):
                            f=float(input("\n[ERROR] Wrong answer. Please try again: "))
                        else:
                            f=ol
                            print("\nThe correct answer is {}. Going back to main menu...\n\n.".format(ol))
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("\n================================\nWelcome to Area Trainer.\n================================")
                            return f
                    total+=score
                    if(score==1):
                        print("\nCorrect answer. You have gained {} point. Going back to main menu...\n\n.".format(score))
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        print("\nCorrect answer. You have gained {} points. Going back to main menu...\n\n.".format(score))
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
            elif(succ==2):
                kms=random.randint(1,12)
                print("\nGenerating question...\n\n.")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                if(kms==1):
                    print("\nWhat is the area of a triangle with base {} and hypotenuse {}? You have 1 try.".format(small,big))
                    ting=round(float((1/2*small)*math.sqrt((big**2)-(small**2))),2)
                    print("\n1:",ting)
                    print("2:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("3:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("4:",float("{0:.2f}".format(random.uniform(500,3000))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==1)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=1
                        print("\nThe correct answer is 1. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==2):
                    print("\nWhat is the area of a triangle with base {} and hypotenuse {}? You have 1 try.".format(small,big))
                    ting=round(float((1/2*small)*math.sqrt((big**2)-(small**2))),2)
                    print("\n1:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("2:",ting)
                    print("3:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("4:",float("{0:.2f}".format(random.uniform(500,3000))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==2)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=2
                        print("\nThe correct answer is 2. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==3):
                    print("\nWhat is the area of a triangle with base {} and hypotenuse {}? You have 1 try.".format(small,big))
                    ting=round(float((1/2*small)*math.sqrt((big**2)-(small**2))),2)
                    print("\n1:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("2:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("3:",ting)
                    print("4:",float("{0:.2f}".format(random.uniform(500,3000))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==3)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=3
                        print("\nThe correct answer is 3. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==4):
                    print("\nWhat is the area of a triangle with base {} and hypotenuse {}? You have 1 try.".format(small,big))
                    ting=round(float((1/2*small)*math.sqrt((big**2)-(small**2))),2)
                    print("\n1:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("2:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("3:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("4:",ting)
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==4)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=4
                        print("\nThe correct answer is 4. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==5):
                    print("\nWhat is the area of a triangle with height {} and hypotenuse {}? You have 1 try.".format(small,big))
                    ting=round(float((1/2*small)*math.sqrt((big**2)-(small**2))),2)
                    print("\n1:",ting)
                    print("2:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("3:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("4:",float("{0:.2f}".format(random.uniform(500,3000))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==1)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=1
                        print("\nThe correct answer is 1. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==6):
                    print("\nWhat is the area of a triangle with height {} and hypotenuse {}? You have 1 try.".format(small,big))
                    ting=round(float((1/2*small)*math.sqrt((big**2)-(small**2))),2)
                    print("\n1:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("2:",ting)
                    print("3:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("4:",float("{0:.2f}".format(random.uniform(500,3000))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==2)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=2
                        print("\nThe correct answer is 2. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==7):
                    print("\nWhat is the area of a triangle with height {} and hypotenuse {}? You have 1 try.".format(small,big))
                    ting=round(float((1/2*small)*math.sqrt((big**2)-(small**2))),2)
                    print("\n1:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("2:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("3:",ting)
                    print("4:",float("{0:.2f}".format(random.uniform(500,3000))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==3)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=3
                        print("\nThe correct answer is 3. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==8):
                    print("\nWhat is the area of a triangle with height {} and hypotenuse {}? You have 1 try.".format(small,big))
                    ting=round(float((1/2*small)*math.sqrt((big**2)-(small**2))),2)
                    print("\n1:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("2:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("3:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("4:",ting)
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==4)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=4
                        print("\nThe correct answer is 4. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==9):
                    print("\nWhat is the area of a triangle with base {} and height {}? You have 1 try.".format(c,d))
                    ting=c*d/2
                    print("\n1:",ting)
                    print("2:",float("{0:.1f}".format(random.uniform(50,500))))
                    print("3:",float("{0:.1f}".format(random.uniform(50,500))))
                    print("4:",float("{0:.1f}".format(random.uniform(50,500))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==1)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=1
                        print("\nThe correct answer is 1. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==10):
                    print("\nWhat is the area of a triangle with base {} and height {}? You have 1 try.".format(c,d))
                    ting=c*d/2
                    print("\n1:",float("{0:.1f}".format(random.uniform(50,500))))
                    print("2:",ting)
                    print("3:",float("{0:.1f}".format(random.uniform(50,500))))
                    print("4:",float("{0:.1f}".format(random.uniform(50,500))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==2)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=2
                        print("\nThe correct answer is 2. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==11):
                    print("\nWhat is the area of a triangle with base {} and height {}? You have 1 try.".format(c,d))
                    ting=c*d/2
                    print("\n1:",float("{0:.1f}".format(random.uniform(50,500))))
                    print("2:",float("{0:.1f}".format(random.uniform(50,500))))
                    print("3:",ting)
                    print("4:",float("{0:.1f}".format(random.uniform(50,500))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==3)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=3
                        print("\nThe correct answer is 3. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                else:
                    print("\nWhat is the area of a triangle with base {} and height {}? You have 1 try.".format(c,d))
                    ting=c*d/2
                    print("\n1:",float("{0:.1f}".format(random.uniform(50,500))))
                    print("2:",float("{0:.1f}".format(random.uniform(50,500))))
                    print("3:",float("{0:.1f}".format(random.uniform(50,500))))
                    print("4:",ting)
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==4)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=4
                        print("\nThe correct answer is 4. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
            else:
                print("\nGoing back to main menu...")
        except:
            print("\n[ERROR] An error occured.\n\nGoing back to main menu...\n\n.")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("\n================================\nWelcome to Area Trainer.\n================================")
    #When the user chooses "Circle" from the main menu.
    else:   
        print("\n================================\nYou have chosen: Circle Area.\n================================")
        print("\nPlease select question type:\n\n1: Short Answer\n2: Multiple Choice\nAny other number: Back to Main Menu")
        try:
            haha=int(input("\nEnter a number from above: "))
            if(haha==1):
                lolol=random.randint(1,5)
                print("\nGenerating question...\n\n.")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                if(lolol==3):
                    score=5
                    h=float(input("\nWhat is the area of a circle with a diameter of {}? You have 5 tries. Answer (2 decimal places): ".format(asdf)))
                    idek=round(float(pie*((asdf/2)**2)),2)
                    while(h!=idek):
                        count+=1
                        score-=1
                        if(count!=5):
                            h=float(input("\n[ERROR] Wrong answer. Please try again: "))
                        else:
                            h=idek
                            print("\nThe correct answer is {}. Going back to main menu...\n\n.".format(idek))
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("\n================================\nWelcome to Area Trainer.\n================================")
                            return h
                    total+=score
                    if(score==1):
                        print("\nCorrect answer. You have gained {} point. Going back to main menu...\n\n.".format(score))
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        print("\nCorrect answer. You have gained {} points. Going back to main menu...\n\n.".format(score))
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                elif(lolol==5):
                    score=5
                    j=float(input("\nWhat is the area of a circle with a circumference of {}? You have 5 tries. Answer (2 decimal places): ".format(asdf)))
                    rekt=round(float(((asdf*asdf)/(4*pie))),2)
                    while(float(j!=rekt)):
                        count+=1
                        score-=1
                        if(count!=5):
                            j=float(input("\n[ERROR] Wrong answer. Please try again: "))
                        else:
                            j=rekt
                            print("\nThe correct answer is {}. Going back to main menu...\n\n.".format(rekt))
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("\n================================\nWelcome to Area Trainer.\n================================")
                            return j
                    total+=score
                    if(score==1):
                        print("\nCorrect answer. You have gained {} point. Going back to main menu...\n\n.".format(score))
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        print("\nCorrect answer. You have gained {} points. Going back to main menu...\n\n.".format(score))
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                else:
                    g=float(input("\nWhat is the area of a circle with a radius of {}? You have 5 tries. Answer (2 decimal places): ".format(asdf)))
                    score=5
                    answ=round(float(pie*(asdf**2)),2)
                    while(g!=answ):
                        count+=1
                        score-=1
                        if(count!=5):
                            g=float(input("\n[ERROR] Wrong answer. Please try again: "))
                        else:
                            g=answ
                            print("\nThe correct answer is {}. Going back to main menu...\n\n.".format(answ))
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("\n================================\nWelcome to Area Trainer.\n================================")
                            return g
                    total+=score
                    if(score==1):
                        print("\nCorrect answer. You have gained {} point. Going back to main menu...\n\n.".format(score))
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        print("\nCorrect answer. You have gained {} points. Going back to main menu...\n\n.".format(score))
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
            elif(haha==2):
                print("\nGenerating question...")
                print("\n.")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                kms=random.randint(1,12)
                if(kms==1):
                    print("\nWhat is the area of a circle with a diameter of {}? You have 1 try.".format(asdf))
                    ting=round(float(pie*((asdf/2)**2)),2)
                    print("\n1:",ting)
                    print("2:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("3:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("4:",float("{0:.2f}".format(random.uniform(500,3000))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==1)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=1
                        print("\nThe correct answer is 1. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==2):
                    print("\nWhat is the area of a circle with a diameter of {}? You have 1 try.".format(asdf))
                    ting=round(float(pie*((asdf/2)**2)),2)
                    print("\n1:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("2:",ting)
                    print("3:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("4:",float("{0:.2f}".format(random.uniform(500,3000))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==2)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=2
                        print("\nThe correct answer is 2. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==3):
                    print("\nWhat is the area of a circle with a diameter of {}? You have 1 try.".format(asdf))
                    ting=round(float(pie*((asdf/2)**2)),2)
                    print("\n1:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("2:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("3:",ting)
                    print("4:",float("{0:.2f}".format(random.uniform(500,3000))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==3)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=3
                        print("\nThe correct answer is 3. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==4):
                    print("\nWhat is the area of a circle with a diameter of {}? You have 1 try.".format(asdf))
                    ting=round(float(pie*((asdf/2)**2)),2)
                    print("\n1:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("2:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("3:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("4:",ting)
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==4)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=4
                        print("\nThe correct answer is 4. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==5):
                    print("\nWhat is the area of a circle with a radius of {}? You have 1 try.".format(asdf))
                    ting=round(float(pie*(asdf**2)),2)
                    print("\n1:",ting)
                    print("2:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("3:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("4:",float("{0:.2f}".format(random.uniform(500,3000))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==1)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=1
                        print("\nThe correct answer is 1. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==6):
                    print("\nWhat is the area of a circle with a radius of {}? You have 1 try.".format(asdf))
                    ting=round(float(pie*(asdf**2)),2)
                    print("\n1:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("2:",ting)
                    print("3:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("4:",float("{0:.2f}".format(random.uniform(500,3000))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==2)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=2
                        print("\nThe correct answer is 2. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==7):
                    print("\nWhat is the area of a circle with a radius of {}? You have 1 try.".format(asdf))
                    ting=round(float(pie*(asdf**2)),2)
                    print("\n1:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("2:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("3:",ting)
                    print("4:",float("{0:.2f}".format(random.uniform(500,3000))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==3)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=3
                        print("\nThe correct answer is 3. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==8):
                    print("\nWhat is the area of a circle with a radius of {}? You have 1 try.".format(asdf))
                    ting=round(float(pie*(asdf**2)),2)
                    print("\n1:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("2:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("3:",float("{0:.2f}".format(random.uniform(500,3000))))
                    print("4:",ting)
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==4)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=4
                        print("\nThe correct answer is 4. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==9):
                    print("\nWhat is the area of a circle with a circumference of {}? You have 1 try.".format(asdf))
                    ting=round(float(((asdf*asdf)/(4*pie))),2)
                    print("\n1:",ting)
                    print("2:",float("{0:.2f}".format(random.uniform(5,50))))
                    print("3:",float("{0:.2f}".format(random.uniform(5,50))))
                    print("4:",float("{0:.2f}".format(random.uniform(5,50))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==1)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=1
                        print("\nThe correct answer is 1. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==10):
                    print("\nWhat is the area of a circle with a circumference of {}? You have 1 try.".format(asdf))
                    ting=round(float(((asdf*asdf)/(4*pie))),2)
                    print("\n1:",float("{0:.2f}".format(random.uniform(5,50))))
                    print("2:",ting)
                    print("3:",float("{0:.2f}".format(random.uniform(5,50))))
                    print("4:",float("{0:.2f}".format(random.uniform(5,50))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==2)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=2
                        print("\nThe correct answer is 2. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                elif(kms==11):
                    print("\nWhat is the area of a circle with a circumference of {}? You have 1 try.".format(asdf))
                    ting=round(float(((asdf*asdf)/(4*pie))),2)
                    print("\n1:",float("{0:.2f}".format(random.uniform(5,50))))
                    print("2:",float("{0:.2f}".format(random.uniform(5,50))))
                    print("3:",ting)
                    print("4:",float("{0:.2f}".format(random.uniform(5,50))))
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==3)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=3
                        print("\nThe correct answer is 3. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                        return aga
                else:
                    print("\nWhat is the area of a circle with a circumference of {}? You have 1 try.".format(asdf))
                    ting=round(float(((asdf*asdf)/(4*pie))),2)
                    print("\n1:",float("{0:.2f}".format(random.uniform(5,50))))
                    print("2:",float("{0:.2f}".format(random.uniform(5,50))))
                    print("3:",float("{0:.2f}".format(random.uniform(5,50))))
                    print("4:",ting)
                    aga=int(input("\nEnter a number from above: "))
                    if(aga==4)or(aga==ting):
                        total+=3
                        print("\nCorrect answer. You have gained 3 points. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================\nWelcome to Area Trainer.\n================================")
                    else:
                        aga=4
                        print("\nThe correct answer is 4. Going back to main menu...\n\n.")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("\n================================")
                        print("Welcome to Area Trainer.")
                        print("================================")
                        return aga
            else:
                print("\nGoing back to main menu...")
        except:
            print("\n[ERROR] An error occured.\n\nGoing back to main menu...\n\n.")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("\n================================\nWelcome to Area Trainer.\n================================")
#Human verification function. The code generates and prints out a random number between 1 and 50000, and the user has to enter the number in order to access to programme.
def ver():
    randin=random.randint(1,50001)
    val=False
    while(val==False):
        try:
            inp=int(input("\nPlease verify that you are not a robot.\n\n{}\n\nEnter the number above: ".format(randin)))
            while(inp!=randin):
                inp=int(input("\n[ERROR] Incorrect. Please try again.\n\nPlease verify that you are not a robot.\n\n{}\n\nEnter the number above: ".format(randin)))
            val==True
            print("\n. . .")
            return inp
        except:
            print("\n[ERROR] Incorrect. Please try again.")
#This function is called after the account validation and human verification are done.
def start():
    loool=0
    while(loool!=6):
        #Calls function "x" which is the main menu, where the user selects an option. The choice is then assigned to variable "loool".
        loool=x()
        #If the user chooses choice 1, 2, or 3.
        if(loool==1)or(loool==2)or(loool==3):
            area(loool)
        #If the user chooses to exit the programme.
        elif(loool==6):
            #Calls the "exitcont" function.
            exitcont()
        #If the user chooses to read more about Area Trainer.
        elif(loool==4):
            about()
        #If the user chooses to play the number guessing game.
        elif(loool==5):
            print("\n================================\nYou have chosen: Guessing Game.\n================================")
            guess()
        #If the choice is invalid, it tells the user to try again.
        else:
            print("\n[ERROR] Invalid choice. Please try again.")
#Shows info about the programme when the user selects "About" from the main menu.
def about():
    print("\n================================\nYou have chosen: About.\n================================")
    print("\n== Area Trainer ==\n\nArea Trainer, made on 18 September 2018, is a programme for you to practise calculating the areas of\nrectangles, triangles, and circles.")
    print("The programme serves as a useful tool for test and examination revision.\nYou can choose to do short answer questions or multiple choice questions.")
    print("\n== Scoring ==\n\nIn short answer questions, you will have five attempts to answer the question correctly.")
    print("\nFirst attempt: 5 points\nSecond attempt: 4 points\nThird attempt: 3 points\nFourth attempt: 2 points\nFifth attempt: 1 point")
    print("\nIn multiple choice questions, you will only have one attempt to answer the question correctly.\nIf your answer is correct, you will gain 3 points.")
    print("\nIf you answer any question wrong, you will not gain any points.")
    print("\n== Guessing Game ==\n\nA built-in game for you to take a break from Area Trainer.\nWhen you select the Guessing Game, the programme generates a number in between 1 to 100,\nand you must guess it within 8 tries.")
    print("You earn 1 point if you guess the correct number.")
    try:
        goback=int(input("\nEnter any other number to go back: "))
        print("\nGoing back to main menu...")
        start()
    except ValueError:
        print("\nGoing back to main menu...")
#Number guessing game.
def guess():
    global total
    xx=random.randint(1,101)
    try:
        yy=int(input("\nGuess a number between 1 and 100. You have 8 tries: "))
        zz=0
        while not(xx==yy):
            zz+=1
            if(not(zz==8)):
                yy=int(input("\n[ERROR] Wrong number. Try again: "))
            else:
                print("\nSorry. The number was",xx,"and you have not guessed it. Better luck next time.")
                print("\nWould you like to continue?")
                aaa=int(input("\nEnter 1 to continue, or any other number to go back to main menu: "))
                if(aaa==1):
                    guess()
                else:
                    print("\nGoing back to main menu...")
                    start()
        total+=1
        print("\nCongratulations. The number was",xx,"and you have guessed it. You have gained 1 point.\n\nWould you like to continue?")
        aaa=int(input("\nEnter 1 to continue, or any other number to go back to main menu: "))
        if(aaa==1):
            guess()
        else:
            print("\nGoing back to main menu...")
            start()
    except ValueError:
        print("\n[ERROR] An error occured.\n\nGoing back to main menu...\n\n.")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        start()
time.sleep(1)
ver()
with open("users.json","r")as f:
    total=json.load(f)[user]["score"]
nowmonth=str(datetime.datetime.today().strftime("%m"))
nowday=str(datetime.datetime.today().strftime("%d"))
weekday=str(datetime.datetime.today().strftime("%w"))
year1=int(datetime.datetime.today().strftime("%Y"))
year0=year1-1
year2=year1+1
print("\nAccess granted. Going to main menu...\n\n.")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("\n================================\nWelcome to Area Trainer.\n================================")
start()
