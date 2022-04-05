# Check if key exists in dictionary and delete that key value from dictionary

def delKey1(d1,key):
    if key in d1:
        d1.pop(key)
    else:
        print(f'{key} not present in Dictionary')


def delKey2(d1,key):
    if key not in d1:
        print(f'{key} not present in Dictionary')
    else:
        del d1[key]


dict1 = {'Java': 200, 'C': 220, 'PHP': 150,'Ruby': 170, 'Go': 250, 'Python': 300}
print("\nDict : ",dict1)

delKey1(dict1,'Ruby')
print("\nAfter Deleting 'Ruby' : ",dict1)


delKey2(dict1,'Go')
print("\nAfter Deleting 'Go' : ",dict1)