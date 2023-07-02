# https://codeforces.com/problemset/problem/1154/A

list_of_nums = list(map(int, input().split()))
list_of_nums.sort()

sum_of_all = list_of_nums[3]

a = sum_of_all - list_of_nums[1]
b = sum_of_all - list_of_nums[2]
c = sum_of_all - list_of_nums[0]

print(f'{a} {b} {c}')
