import sys

# num of soldiers
soldiers_num = int(input())
soldiers_height = list(map(int, input().split()))

# predefine min and max
minimum_pos = None
maximum_pos = None
minimum_height = sys.maxsize
maximum_height = -sys.maxsize
result = 0

# finding the min and max height soldiers and their positions
for i in range(0, soldiers_num):
    if soldiers_height[i] <= minimum_height:
        minimum_height = soldiers_height[i]
        minimum_pos = i
    if soldiers_height[i] > maximum_height:
        maximum_height = soldiers_height[i]
        maximum_pos = i

# calculating the steps required
if minimum_pos > maximum_pos:
    result = (soldiers_num - minimum_pos) + maximum_pos - 1
else:
    result = (soldiers_num - minimum_pos) + (maximum_pos - 2)

print(result)
