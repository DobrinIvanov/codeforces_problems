# https://codeforces.com/problemset/problem/151/A

n_friends, k_bottles, l_ml, c_limes, d_slices, p_grams, nl_ml, np_salt = map(int, input().split())

total_mililitres = k_bottles * l_ml


total_lime_slices_toasts = c_limes * d_slices
drinks_toasts = total_mililitres // nl_ml
salt_toasts = p_grams // np_salt

result = min(salt_toasts, drinks_toasts, total_lime_slices_toasts) // n_friends

print(result)
