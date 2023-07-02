# https://codeforces.com/problemset/problem/1352/A

test_cases = int(input())

for t in range(test_cases):
    number = int(input())
    num_of_summands = 0
    list_of_summands = list()

    if number <= 10:
        print(1)
        print(number)
        continue

    for i in range(4, 0, -1):
        curr_round = 10 ** i
        summand_check = number // curr_round
        if summand_check > 0:
            num_of_summands += 1
            list_of_summands.append(curr_round * summand_check)
        number = number % curr_round
        if number == 0:
            print(num_of_summands)
            print(' '.join(map(str, list_of_summands)))
            break
        elif number <= 10:
            num_of_summands += 1
            list_of_summands.append(number)
            print(num_of_summands)
            print(' '.join(map(str, list_of_summands)))
            break

