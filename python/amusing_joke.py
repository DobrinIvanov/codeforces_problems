# https://codeforces.com/problemset/problem/141/A

guest_name = input()
host_name = input()
letters_pile = [*input()]

all_names_letters = [*guest_name] + [*host_name]
not_complete = False

for letter in all_names_letters:
    if letter in letters_pile:
        letters_pile.remove(letter)
    else:
        not_complete = True
        break

if not_complete or len(letters_pile) > 0:
    print('NO')
else:
    print('YES')
