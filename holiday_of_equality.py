# https://codeforces.com/problemset/problem/758/A

citizens = int(input())
burles_per_citizen = list(map(int, input().split()))

richest_citizen_brules = max(burles_per_citizen)

burles_required = (richest_citizen_brules * citizens) - sum(burles_per_citizen)

print(burles_required)
