# Sort tuple by 2nd item tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))



tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29),('f',25),('s',9))
list1 = list(tuple1)
print(f'Original Tuple : {tuple1}')

list_len = len(list1)
for i in range(list_len-1):
    min = i

    for j in range(i+1,list_len):
        if list1[j][1] < list1[min][1]:
            min = j
        
    list1[min],list1[i] = list1[i],list1[min]


res = tuple(list1)
print(f'Sorted Tuple : {res}')

