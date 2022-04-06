# Return new set of identical items from two sets


def simItems(set1,set2):
    res = set()
    for a in set1:
        for b in set2:
            if a == b:
                res.add(a)
           
    return res

set1 = {"Raj",92, 45, "Soham", 81, 72, "Ravi"}
set2 = {"Soham", 45, "Rajat", "Vikas","Ravi",92}
print(f'Set 1 : {set1}')
print(f'Set 2 : {set2}')

result = simItems(set1,set2)
print(f'\nIdentical items from two sets : {result}')