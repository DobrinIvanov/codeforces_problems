# https://codeforces.com/problemset/problem/1409/A


test_cases = int(input())

for t in range(test_cases):
    a, b = map(int, input().split())

    result = 0
    difference = abs(a - b)
    for i in range(10, 0, -1):
        remainder = difference % i
        result += difference // i
        difference = remainder

    print(result)
