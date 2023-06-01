# https://codeforces.com/problemset/problem/1352/A

test_cases = int(input())

num_of_summands = 0

for t in range(test_cases):
    number = int(input())
    if number <= 10:
        print(1)
        print(number)
        break
    for i in range(4, 0, -1):
        curr_round = i * 10

    # if number <= 10:
    #     print(1)
    #     print(number)
    # elif number <= 100:
    #     pass
