# https://codeforces.com/contest/996/problem/A

n_dollars = int(input())

min_bills = 0

denominations = [100, 20, 10, 10, 5, 1]

for bill in denominations:
    min_bills += n_dollars // bill
    n_dollars = n_dollars % bill
    if n_dollars == 0:
        break


print(min_bills)
