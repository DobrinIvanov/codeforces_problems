# https://codeforces.com/contest/443/problem/A

set_as_string = input()
set_as_string = set_as_string.strip('{').strip('}')
if not set_as_string:
    print(0)
else:
    antons_set = set(set_as_string.split(', '))
    print(len(antons_set))
