import random
from os import system, name
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
n = int(input())
grid = [[0 for _ in range(n)] for _ in range(n)]
grid[random.randrange(n)][random.randrange(n)] = [2, 4][random.randrange(5) == 4]
spaces = []
for i in range(n):
    for j in range(n):
        if not grid[i][j]:
            spaces.append((i, j))
r, c = random.choice(spaces)
grid[r][c] = [2, 4][random.randrange(5) == 4]
max_num = 4
while True:
    d = len(str(max_num))
    for i in range(n):
        print(' '.join((d - len(str(j))) * ' ' + str(j) for j in grid[i]))
    direction = input()
    changed = False
    if direction == 'd':
        for i in range(n):
            curr_num, curr_col = grid[i][-1], n - 1
            for j in range(n - 2, -1, -1):
                if grid[i][j]:
                    if grid[i][j] == curr_num:
                        grid[i][j], grid[i][curr_col] = 0, 2 * curr_num
                        max_num = max(max_num, grid[i][curr_col])
                        curr_num, changed = 0, True
                        curr_col -= 1
                    else:
                        curr_num, curr_col = grid[i][j], j
            total = list(filter(bool, grid[i]))
            if grid[i] != [0] * (n - len(total)) + total:
                changed = True
            grid[i] = [0] * (n - len(total)) + total
    elif direction == 'a':
        for i in range(n):
            curr_num, curr_col = grid[i][0], 0
            for j in range(1, n):
                if grid[i][j]:
                    if grid[i][j] == curr_num:
                        grid[i][j], grid[i][curr_col] = 0, 2 * curr_num
                        max_num = max(max_num, grid[i][curr_col])
                        curr_num, changed = 0, True
                        curr_col += 1
                    else:
                        curr_num, curr_col = grid[i][j], j
            total = list(filter(bool, grid[i]))
            if grid[i] != total + [0] * (n - len(total)):
                changed = True
            grid[i] = total + [0] * (n - len(total))
    elif direction == 's':
        for j in range(n):
            curr_num, curr_row = grid[-1][j], n - 1
            for i in range(n - 2, -1, -1):
                if grid[i][j]:
                    if grid[i][j] == curr_num:
                        grid[i][j], grid[curr_row][j] = 0, 2 * curr_num
                        max_num = max(max_num, grid[curr_row][j])
                        curr_num, changed = 0, True
                        curr_row -= 1
                    else:
                        curr_num, curr_row = grid[i][j], i
            total = list(r[j] for r in grid if r[j])
            if [grid[_][j] for _ in range(n)] != total:
                changed = True
            for _ in range(n - len(total)):
                grid[_][j] = 0
            for _ in range(len(total)):
                grid[n - len(total) + _][j] = total[_]
    elif direction == 'w':
        for j in range(n):
            curr_num, curr_row = grid[0][j], 0
            for i in range(1, n):
                if grid[i][j]:
                    if grid[i][j] == curr_num:
                        grid[i][j], grid[curr_row][j] = 0, 2 * curr_num
                        max_num = max(max_num, grid[curr_row][j])
                        curr_num, changed = 0, True
                        curr_row += 1
                    else:
                        curr_num, curr_row = grid[i][j], i
            total = list(r[j] for r in grid if r[j])
            if [grid[_][j] for _ in range(n)] != total:
                changed = True
            for _ in range(len(total)):
                grid[_][j] = total[_]
            for _ in range(n - len(total)):
                grid[len(total) + _][j] = 0
    if changed:
        spaces = []
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    spaces.append((i, j))
        if not spaces:
            print("Game Over!")
            break
        r, c = random.choice(spaces)
        grid[r][c] = [2, 4][random.randrange(5) == 4]
        clear()
