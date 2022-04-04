# Count Occurance of each element from list
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

def countlist(l1):
    count = {}
    for i in l1:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        
        
    return count


list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
countElement = countlist(list1)
for key,value in countElement.items():
    print(f'count of {key} = {value} ')

