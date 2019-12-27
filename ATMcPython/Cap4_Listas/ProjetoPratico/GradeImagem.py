grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

grid2 = [[],[],[],[],[],[]]

for i in range(len(grid)):
    grid2[0].append(grid[i][0])

for i in range(len(grid)):
    grid2[1].append(grid[i][1])

for i in range(len(grid)):
    grid2[2].append(grid[i][2])

for i in range(len(grid)):
    grid2[3].append(grid[i][3])

for i in range(len(grid)):
    grid2[4].append(grid[i][4])

for i in range(len(grid)):
    grid2[5].append(grid[i][5])


for i in grid2:
    print(i)










