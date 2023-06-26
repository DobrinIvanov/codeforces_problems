# https://codeforces.com/problemset/problem/432/A

n, k = map(int, input().split())
students_participation_count = list(map(int, input().split()))

total_eligible = 0

for c in students_participation_count:
    if 5 - c >= k:
        total_eligible += 1

result = total_eligible // 3
print(result)
