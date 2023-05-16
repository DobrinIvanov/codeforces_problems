# 1 <= n <= 100 - total game levels
n_levels = int(input())

x_levels_p = list(map(int, input().split()))
y_levels_q = list(map(int, input().split()))

all_levels_passed = list(set(x_levels_p[1::] + y_levels_q[1::]))

passed_all_levels = True
for i in range(1, n_levels + 1):
    if i not in all_levels_passed:
        print("Oh, my keyboard!")
        passed_all_levels = False
        break

if passed_all_levels:
    print("I become the guy.")
