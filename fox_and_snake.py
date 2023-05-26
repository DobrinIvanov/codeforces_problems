# https://codeforces.com/problemset/problem/510/A

n, m = map(int, input().split())

snake_table = []

forward = True
for row in range(n):
    row_list = list()
    if row % 2 == 0:
        for i in range(m):
            row_list.append('#')
        snake_table.append(row_list)
    else:
        for i in range(m - 1):
            row_list.append('.')
        row_list.append('#')
        if forward:
            snake_table.append(row_list)
            forward = False
        else:
            row_list.reverse()
            snake_table.append(row_list)
            forward = True

for row in snake_table:
    print(''.join(row))


