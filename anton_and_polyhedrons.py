# https://codeforces.com/problemset/problem/785/A

figures_num = int(input())
total_num_faces = 0

for figure in range(figures_num):
    name = input()
    # to be continued
    if name == 'Tetrahedron':
        total_num_faces += 4
    elif name == 'Cube':
        total_num_faces += 6
    elif name == 'Octahedron':
        total_num_faces += 8
    elif name == 'Dodecahedron':
        total_num_faces += 12
    elif name == 'Icosahedron':
        total_num_faces += 20

print(total_num_faces)

# Alternative solution can be done with "match-case" in Python 3.10 and 3.11
