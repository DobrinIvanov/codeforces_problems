# https://codeforces.com/problemset/problem/427/A

events = int(input())

available_officers = 0
unresolved_crimes = 0

list_event_integers = list(map(int, input().split()))
for event_integer in list_event_integers:
    if event_integer == -1:
        if available_officers > 0:
            available_officers -= 1
        else:
            unresolved_crimes += 1
    else:
        available_officers += event_integer

print(unresolved_crimes)
