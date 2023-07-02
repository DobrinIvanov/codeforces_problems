# https://codeforces.com/problemset/problem/381/A

cards_count = int(input())
cards_numbers = list(map(int, input().split()))

sereja_score, dima_score = 0, 0
turns_counter = 0
while len(cards_numbers) > 0:

    first_card = cards_numbers[0]
    last_card = cards_numbers[::-1][0]

    if first_card > last_card:
        if turns_counter % 2 == 0:
            sereja_score += first_card
        else:
            dima_score += first_card
        cards_numbers.pop(0)

    else:
        if turns_counter % 2 == 0:
            sereja_score += last_card
        else:
            dima_score += last_card
        cards_numbers.pop(len(cards_numbers)-1)

    turns_counter += 1


print(sereja_score, dima_score)
