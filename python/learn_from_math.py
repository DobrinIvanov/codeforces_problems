# https://codeforces.com/problemset/problem/472/A


def express_as_sum_of_composites(n):
    # Helper function to check if a number is composite ( all but prime numbers )
    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False

    # Find two composite numbers that add up to n
    for i in range(4, n):
        if is_composite(i) and is_composite(n - i):
            return i, n - i

    return None


# Test the function
n = int(input())
result = express_as_sum_of_composites(n)

if result:
    x, y = result
    print(x, y)
else:
    print("No solution exists for the given input.")
