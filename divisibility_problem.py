# https://codeforces.com/contest/1328/problem/A

test_cases = int(input())

for case in range(test_cases):
    a, b = map(int, input().split())

    moves = 0

    if a % b == 0:
        print(0)
    else:
        result = b - (a % b)
        print(result)
