k = int(input())
l = int(input())
m = int(input())
n = int(input())

dragons = int(input())

result = 0

for dragon in range(1, dragons + 1):
    if dragon % k == 0 or dragon % l == 0 or dragon % m == 0 or dragon % n == 0:
        result += 1

print(result)
