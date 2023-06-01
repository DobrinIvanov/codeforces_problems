# https://codeforces.com/problemset/problem/155/A

num_of_contests = int(input())

points_earned = list(map(int, input().split()))

amazing_performances = 0
best_score, worst_score = points_earned[0], points_earned[0]

for contest_score in points_earned[1::]:
    if contest_score > best_score:
        best_score = contest_score
        amazing_performances += 1
    elif contest_score < worst_score:
        worst_score = contest_score
        amazing_performances += 1

print(amazing_performances)
