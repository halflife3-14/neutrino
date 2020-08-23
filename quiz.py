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
        
print(response)
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

  