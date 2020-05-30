# input the number of items in group a and b

from collections import defaultdict

# d = defaultdict(list)
# a, b = map(int, input().split())
# list1 = []
#
# # defaultdict(<class 'list'>, {'a': [1, 2, 4], 'b': [3, 5]})
# for i in range(a):
#     d[input()].append(i+1)
#
# for i in range(b):
#     list1 += input()
#
# for i in list1:
#     if i in d:
#         print(" ".join(map(str, d[i])))
#     else:
#         print(-1)

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(1, n + 1):
    d[input()].append(str(i))
print(d)
for i in range(m):
    print(' '.join(d[input()]) or -1)
