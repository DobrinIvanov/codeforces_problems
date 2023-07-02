# https://codeforces.com/problemset/problem/96/A

players_string = input()
counter = 1

current_player = players_string[0]
dangerous = False
for each in players_string[1::]:
    if current_player == each:
        counter += 1
        if counter == 7:
            dangerous = True
            break
    else:
        counter = 1
        current_player = each


if dangerous:
    print('YES')
else:
    print('NO')


