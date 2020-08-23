
def quiz():
    with open("info.txt","r") as info:
        data = info.readlines()
        for lines in data:
            print(lines,sep='\n')
 
 
    response=[];  
 
    with open("quiz.txt","r") as quiz:
        data= quiz.readlines()
        for qset in data:
            q = qset.split(":")
            for lines in q :
                print(lines,sep='\n')
            ans = input("Enter your response :")
            response.append(ans)       
        
    
    answers=[];
    i=0;
    score=0;
    with open("ans.txt","r") as ans:
        dataans = ans.readlines()
        for oneans in dataans:
            answers= oneans.split(":")
            
        for lists in answers:
            if lists == response[i]:
                score=score+1;
                i=i+1;   
    return score


def signin():
    fhandle= open("Database.txt","a+")
    username = input("Enter your username :")
    password = input("Enter your password :")
    score = quiz();
    delim=":";
    string1 = [username,password,str(score)]
    print("Your overall score is :",score)
    print("Login again to see other features")
    fhandle.write("\n")
    x =delim.join(string1)
    fhandle.write(x)
 

def login():
    register={};
    with open ("Database.txt","r") as database:
       users=database.readlines()
       for members in users:
        temp=members.split(":")
        temp2=[temp[1],temp[2]]
        register[temp[0]]=temp2  
        
    username=input("Enter your username :")
    password=input("Enter your password :")
    for keys1 in register.keys():
        if username == keys1:
            if password == register[keys1][0]:
                print("logged in")
                print("Your score is",register[keys1][1])
                qeditreq=input("Do you want to edit the questions (y/n):")
                if qeditreq == "y":
                    qedit()
                    exit()
                exit()
        

    print("Username or Password error")

def qedit():
    qwrite=open("quiz.txt","w")
    count =0;
    temp=[];
    while count < 5:
        tempque=input("Enter the question :")
        choise1=input("Enter the first choise :")
        choise2=input("Enter the second choise :")
        choise3=input("Enter the third choise :")
        choise4=input("Enter the fourth choise :")
        temp=[tempque,choise1,choise2,choise3,choise4]
        delim=":";
        qwrite.write(delim.join(temp))
        qwrite.write("\n")
        count=count + 1;
    awrite=open("ans.txt","w")
    ans1=input("Answer for first question :")
    ans2=input("Answer for second question :")
    ans3=input("Answer for third question :")
    ans4=input("Answer for fouth question :")
    ans5=input("Answer for fifth question :")

    temp=[ans1,ans2,ans3,ans4,ans5]
    awrite.write(delim.join(temp))

euser = input("Are you an existing user (y/n) :")
 
if euser == "y":
    login()
if euser == "n":
    signin()

