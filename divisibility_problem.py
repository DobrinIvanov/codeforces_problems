test_cases = int(input())

for case in range(test_cases):
    a, b = map(int, input().split())

    moves = 0

    if a % b == 0:
        print(0)
    else:
        result = b - (a % b)
        print(result)

    # while a % b != 0:
    #     a += 1
    #     moves += 1
    #
    # print(moves)
    # a = 17
    # b = 5
    # b - (a % b) = 5 - (17 % 5)
