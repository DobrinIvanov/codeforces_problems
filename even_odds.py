# https://codeforces.com/problemset/problem/318/A

# # # # # slow solution I thought of, which is very impractical

# n_number, k_position = map(int, input().split())
#
# odd_list, even_list, final_list = [], [], []
#
# for num in range(1, n_number + 1):
#     if num % 2 == 1:
#         odd_list.append(num)
#     else:
#         even_list.append(num)
#
# final_list = odd_list + even_list
#
# print(final_list[k_position - 1])

# # # # # solution with a formula ( Google help)
n_number, k_position = map(int, input().split())

if k_position <= (n_number + 1) // 2:
    result = 2 * k_position - 1
else:
    result = 2 * (k_position - (n_number + 1) // 2)

print(result)
