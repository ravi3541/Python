# Merge two dictionaries into one and rename dictionary key name

def merge1(d1, d2):
    res = d1.update(d2)
    return res


def renameKey(d1):
    d1["C++"] = d1.pop('C')
    



dict1 = {'Java': 200, 'C': 220, 'PHP': 150}
dict2 = {'Ruby': 170, 'Go': 250, 'Python': 300}


merge1(dict1, dict2)
print("Merged using update() : ", dict1)

renameKey(dict1)
print("After Renaming key 'C' to 'C++' ",dict1)