# https://codeforces.com/contest/1836/problem/A

test_cases = int(input())


for t in range(test_cases):
    not_possible = False
    n = int(input())
    robot_reports = list(map(int, input().split()))
    curr_count = robot_reports.count(0)

    for i in range(1, 101):
        new_count = robot_reports.count(i)
        if new_count > curr_count:
            not_possible = True
            break
        curr_count = new_count

    if not_possible:
        print('NO')
    else:
        print('YES')
