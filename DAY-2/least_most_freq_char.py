input_str = "least/most occuring character in string"

count_char = {}
for key in input_str:
    if key in count_char:
        count_char[key] += 1
    else:
        count_char[key] = 1


k = list(count_char.keys())
v = list(count_char.values())
print(k, "\n", v)

print("least occuring character : " + k[v.index(min(v))] + ".")
print("most occuring character : " + k[v.index(max(v))] + ".")
