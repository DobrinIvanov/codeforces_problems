# https://codeforces.com/problemset/problem/1367/A

test_cases = int(input())

for t in range(test_cases):

    result_string = input()
    og_string = ''

    if len(result_string) == 2:
        og_string = result_string
        print(og_string)
        continue

    else:
        og_string = result_string[0:2]
        for i in range(3, len(result_string)+1, 2):
            og_string += result_string[i]
        print(og_string)
