# https://codeforces.com/problemset/problem/490/A

children = int(input())
children_skills = list(map(int, input().split()))

mathematicians_idx = []
programmers_idx = []
athletes_idx = []

for i, v in enumerate(children_skills):
    if v == 1:
        programmers_idx.append(i)
    elif v == 2:
        mathematicians_idx.append(i)
    elif v == 3:
        athletes_idx.append(i)

teams = min(len(mathematicians_idx), len(programmers_idx), len(athletes_idx))

print(teams)
if teams > 0:
    for i in range(teams):
        print(programmers_idx[i] + 1, mathematicians_idx[i] + 1, athletes_idx[i] + 1)
