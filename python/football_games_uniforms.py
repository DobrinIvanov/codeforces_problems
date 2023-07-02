# https://codeforces.com/contest/268/problem/A

team_num = int(input())
matrix_of_uniforms = []
for each_team in range(team_num):
    matrix_of_uniforms.append(list(map(int, input().split())))

result = 0
for team in range(team_num):
    home_uniform = matrix_of_uniforms[team][0]
    for i in range(team_num):
        temp_value = matrix_of_uniforms[i][1]
        if temp_value == home_uniform:
            result += 1

print(result)
