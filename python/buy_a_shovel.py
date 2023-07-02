# https://codeforces.com/problemset/problem/732/A

shovel_cost, extra_coin = map(int, input().split())
result = None
result_found = False

for i in range(1, 11):
    if result_found:
        break
    required_amount = i * shovel_cost

    coins_num = 0
    coins_value = 0
    while coins_value <= required_amount and not result_found:
        coins_num += 1
        coins_value += 10
        if required_amount % coins_value == 0 or (required_amount - extra_coin) % coins_value == 0:
            result = i
            result_found = True

print(result)
