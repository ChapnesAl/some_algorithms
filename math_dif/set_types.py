"""множества"""

finite_set = {1, 2, 3, 4, 5}
infinite_set = {1, 2, 3, 4, ...}

print(infinite_set)

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3}
res = set1 >= set2
print(res)

element = 3
if element in set2:
    print(True)