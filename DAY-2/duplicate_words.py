#Print duplicate words with count
    
in_str="Fear leads to anger anger leads to hatred hatred leads to conflict conflict leads to suffering"

words=in_str.lower().split(" ")

for i in range(0,len(words)):
    count=1
    for j in range(i+1,len(words)):
        if words[i]==words[j]:
            count+=1
            words[j]=0
    
    if count>1 and  words[i]!=0: 
        print(words[i]," ",count)
        


