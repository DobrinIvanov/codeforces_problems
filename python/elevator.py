# https://codeforces.com/problemset/problem/120/A

with open('input.txt') as input_file:
    door, rail = input_file.readlines()
    if 'front' in door:
        if '1' in rail:
            result = 'L'
        else:
            result = 'R'
    else:
        if '1' in rail:
            result = 'R'
        else:
            result = 'L'

result_file = open("output.txt", "w+")
result_file.write(result)
result_file.close()
