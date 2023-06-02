# https://codeforces.com/problemset/problem/581/A

red, blue = map(int, input().split())

difference = abs(red - blue)
diff_socks_days = min(list((red, blue)))
same_socks_days = difference // 2

print(f'{diff_socks_days} {same_socks_days}')
