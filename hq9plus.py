# https://codeforces.com/problemset/problem/133/A

program_input = input()

program_set = ('H', 'Q', '9')
has_output = False

for char in program_input:
    if char in program_set:
        print('YES')
        has_output = True
        break

if not has_output:
    print('NO')
