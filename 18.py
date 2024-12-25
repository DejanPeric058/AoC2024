import collections
# A PART
with open("18.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')

wall, clear, goal = "#", ".", "*"
width, height = 71, 71
grid = [['.' for _ in range(width)] for _ in range(height)]
for c in commands[:1024]:
    a,b = c.split(',')
    a,b = int(a), int(b)
    grid[b][a] = '#'
grid[height-1][width-1] = '*'
#print(grid)

def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
path = bfs(grid, (0, 0))
# for a,b in path:
#     grid[b][a] = 'O'
#print(grid)
print(len(path)-1)

# PART B

for c in commands[1024:]:
    a,b = c.split(',')
    a,b = int(a), int(b)
    grid[b][a] = '#'
    path = bfs(grid, (0, 0))
    if path is None:
        break
print(a,b)