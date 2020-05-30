from collections import Counter

#  number of shoe pairs in the shop
#  size of all the shoes
#  nUmber of customers
#  what size did they buy and how much they paid

x = int(input())
n = Counter(map(int, input().split()))
n_c = int(input())

income = 0

for _ in range(n_c):
    size, price = map(int, input().split())
    if n[size]:
        income += price
        n[size] -= 1

print(income)


def income_count(num_shoes, shoe_sizes, num_cust):
    pass
