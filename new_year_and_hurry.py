# https://codeforces.com/problemset/problem/750/A

num_of_problems, minutes_required = map(int, input().split())

minutes_available = 4 * 60 - minutes_required
problems_solved = 0

for i in range(1, num_of_problems + 1):
    if minutes_available >= i * 5:
        minutes_available -= i * 5
        problems_solved += 1
    else:
        break

print(problems_solved)
