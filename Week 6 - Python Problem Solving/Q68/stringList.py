# Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.


def delStrList(s1, l1):
    final_list = []
    for i in range(len(l1)):

        str = l1[i]
        split_s = []
        for s in str:
            if s not in s1:
                split_s.append(s)
            #print(f'Split s = {split_s}')
        # print("--------------------------",split_s)

        final_list_elem = ""
        for i in split_s:
            final_list_elem += i

        final_list.append(final_list_elem)
    #print(f'Final list elements= {final_list}')
    return final_list


list1 = []

print("Enter 10 list elements : ")
for i in range(5):
    elem = input()
    list1.append(elem)

str1 = input("Enter a string : ")
print(f'original list = {list1}')
print(f'\n string to remove letters from list = {str1}')


final_list = delStrList(str1, list1)
print(f'\n final list = {final_list}')
