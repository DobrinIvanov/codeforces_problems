# https://codeforces.com/problemset/problem/1343/B

test_cases = int(input())

for t in range(test_cases):

    total_numbers = int(input())
    if total_numbers % 4 != 0:
        print('NO')
        continue

    even_half = list()
    odd_half = list()

    for even_num in range(1, total_numbers // 2 + 1):
        even_half.append(even_num*2)

    for odd_num in range(1, total_numbers // 2):
        odd_half.append(odd_num*2 - 1)

    result_list = even_half + odd_half

    last_num = sum(even_half) - sum(odd_half)
    result_list.append(last_num)

    print('YES')
    print(' '.join(map(str, result_list)))


