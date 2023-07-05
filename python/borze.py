# https://codeforces.com/problemset/problem/32/B

borze_code = input()
final_number = ''

temp_symbol_check = ''

for char in borze_code:
    temp_symbol_check += char
    if temp_symbol_check == '.':
        final_number += '0'
    elif len(temp_symbol_check) == 1:
        continue
    elif temp_symbol_check == '-.':
        final_number += '1'
    elif temp_symbol_check == '--':
        final_number += '2'

    temp_symbol_check = ''

print(final_number)
