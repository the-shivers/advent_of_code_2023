with open('input.txt') as file:
    lines = [list(line.strip()) for line in file] 

def dfs(x, y, z, grid, pt1):
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid): return 0
    if int(grid[y][x]) != z: return 0
    if pt1: grid[y][x] = -1
    if z == 9: return 1
    return (
        dfs(x, y - 1, z + 1, grid, pt1) + dfs(x + 1, y, z + 1, grid, pt1) + 
        dfs(x, y + 1, z + 1, grid, pt1) + dfs(x - 1, y, z + 1, grid, pt1)
    )

pt1 = pt2 = 0
for y, line in enumerate(lines):
    for x, chr in enumerate(line):
        if chr == '0':
            pt1 += dfs(x, y, 0, [l[:] for l in lines], True)
            pt2 += dfs(x, y, 0, lines, False)
print(f"Part 1: {pt1}\nPart 2: {pt2}")