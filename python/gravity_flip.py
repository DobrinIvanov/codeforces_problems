# https://codeforces.com/problemset/problem/405/A

columns_num = int(input())
columns_count = list(map(int, input().split()))

print(' '.join(map(str, sorted(columns_count))))
