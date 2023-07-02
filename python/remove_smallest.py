# https://codeforces.com/problemset/problem/1399/A

test_cases = int(input())

for t in range(test_cases):
    possible = True

    length = int(input())
    num_list = [abs(x) for x in map(int, input().split())]
    num_list.sort()
    temp_num = num_list[0]
    for num in num_list[1::]:
        if abs(temp_num - num) >= 2:
            possible = False
            break
        temp_num = num

    if possible:
        print('YES')
    else:
        print('NO')
