
List = [0, 1, 20, 0, 0, 3, 5, 0]
positions = []
pairs = []
dictionary = {}

for i in range(0, len(List)):
    if List[i] in dictionary:
        dictionary[List[i]].append(i)
    else:
        dictionary[List[i]] = [i]

for number, pos in dictionary.items():
    if len(pos) > 1:
        positions = pos
# multiple repeated numbers?

for num in positions:
    for sec_num in positions:
        if num < sec_num:
            pairs.append([num, sec_num])

print(dictionary)
print(pairs)

# n/2(0+len(list)) number of pairs
