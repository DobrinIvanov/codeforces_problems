# https://codeforces.com/problemset/problem/266/B

children, time = map(int, input().split())
initial_arrangement = input()

current_arrangement = initial_arrangement[:]
skip_line = False

for t in range(time):
    temp_list = list()

    for idx in range(0, children):
        if skip_line:
            skip_line = False
            continue
        if idx == children - 1:
            temp_list.append(current_arrangement[idx])
        elif current_arrangement[idx] == 'B' and current_arrangement[idx + 1] == 'G':
            temp_list.append('G')
            temp_list.append('B')
            skip_line = True
        else:
            temp_list.append(current_arrangement[idx])

    current_arrangement = temp_list[:]

print(''.join(current_arrangement))
