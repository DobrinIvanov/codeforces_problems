# https://codeforces.com/problemset/problem/160/A

total_num_of_coins = int(input())
list_of_coins = list(map(int, input().split()))

half = sum(list_of_coins) / 2
value_in_my_pocket = 0
my_coin_count = 0

list_of_coins = sorted(list_of_coins, reverse=True)

for coin_value in list_of_coins:
    value_in_my_pocket += coin_value
    my_coin_count += 1
    if value_in_my_pocket > half:
        print(my_coin_count)
        break
