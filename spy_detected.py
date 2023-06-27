# https://codeforces.com/problemset/problem/1512/A

test_cases = int(input())

single_occurance_index = None

for t in range(test_cases):
    length = int(input())
    nums = list(map(int, input().split()))
    for num in range(0, len(nums)):
        curr_value = nums[num]
        if nums.count(curr_value) == 1:
            single_occurance_index = num + 1
            break

    print(single_occurance_index)
