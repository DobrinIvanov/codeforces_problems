# https://codeforces.com/problemset/problem/1335/A

test_cases = int(input())

for t in range(test_cases):
    num_of_candies = int(input())

    if num_of_candies % 2 == 0:
        ways_of_distr = (num_of_candies / 2) - 1
    else:
        ways_of_distr = num_of_candies // 2

    print(int(ways_of_distr))
