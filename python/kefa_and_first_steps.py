# https://codeforces.com/problemset/problem/580/A

n = int(input())

money_made = list(map(int, input().split()))
overall_streak = 1
curr_streak = 1


curr_day = money_made[0]
for day in money_made[1::]:
    if day >= curr_day:
        curr_streak += 1
        if curr_streak > overall_streak:
            overall_streak = curr_streak
    else:
        curr_streak = 1
    curr_day = day

print(overall_streak)
