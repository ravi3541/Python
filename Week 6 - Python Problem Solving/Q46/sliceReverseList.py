# Slice list into 3 chunks and reverse each chunks
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]


def sliceAndReverse(l1):

    temp = []
    res = []

    for i in range(len(l1)):
        temp.append(l1[i])
        # print(f'temp in loop = {temp}')
        # print(f'Result in loop = {res}')
        if (i+1) % 3 == 0 :
            temp.reverse()
            res.append(temp)
            # print(f'temp in if  = {temp}')
            # print(f'Result inside if = {res}')
            temp=[]

    print(f'list after Slicing and reversing : {res}')


sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
sliceAndReverse(sample_list)
