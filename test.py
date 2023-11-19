import copy
l1 = [1,2,[2.1,2.2,2.3]]
l2 = copy.deepcopy(l1)
l1[2][0] = 1.101
print(l1)
print(l2)