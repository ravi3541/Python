#Get only unique items from dictionary


def uniqueDict(l1):
    s1=set()

    for dic in l1:
        for val in dic.items():
            s1.add(val)    
    res = list(s1)

    #res = list(set(val for dict in l1 for val in dict.items()))
    print("Unique values : ",res)





list1 = [{'name':'Soham','class':'10th','div':'B','hobby':'gaming','score':538},
        {'name':'Raj','class':'10th','div':'B','hobby':'reading','score':538}]



uniqueDict(list1)


