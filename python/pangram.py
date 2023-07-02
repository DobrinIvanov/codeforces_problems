# https://codeforces.com/contest/520/problem/A

num_of_chars = int(input())
string_to_check = input().lower()

if len(string_to_check) < 26:
    print('NO')
else:
    list_of_chars = list()
    for char in string_to_check:
        list_of_chars.append(char)
    if len(set(list_of_chars)) == 26:
        print('YES')
    else:
        print('NO')
