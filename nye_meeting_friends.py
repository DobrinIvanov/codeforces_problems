# https://codeforces.com/problemset/problem/723/A

positions_list = list(map(int, input().split()))
positions_list.sort()

steps = (abs(positions_list[0] - positions_list[1])) + abs((positions_list[2] - positions_list[1]))

print(steps)