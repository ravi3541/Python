# Take two list and Iterate both list simultaneously and print output

l1 = ['Mango','Orange','Banana','grapes','Apple']
l2 = ['Pune','Mumbai','Kolkata','Delhi','Nashik']

if len(l1) == len(l2):
    
    for i in range(len(l1)):
        print(f'({l1[i]}, {l2[i]})')

else:
    print("Length of both lists should be same")

