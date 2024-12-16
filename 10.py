# A PART
with open("10.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
N, M = len(commands), len(commands[0])
c = [['#' for _ in range(M+2)]]
c += [['#'] + [a for a in row] + ['#'] for row in commands]
c += [['#' for _ in range(M+2)]]
#print(c)

zeros = []
for i, row in enumerate(c):
    for j, a in enumerate(row):
        if a == '0':
            zeros.append((i,j))
#print(zeros)

def find_next(i,j,k):
    global c
    k = str(k)
    next = []
    if c[i-1][j] == k:
        next.append((i-1,j))
    if c[i+1][j] == k:
        next.append((i+1,j))
    if c[i][j-1] == k:
        next.append((i,j-1))
    if c[i][j+1] == k:
        next.append((i,j+1))
    return next

for z in zeros:
    next = [z]
    for k in range(1,10):
        new_next = []
        for i,j in next:
            #print(next, k)
            new_next += find_next(i,j,k)
        next = new_next
    counter += len(set(next))

print(counter)

# PART B

counter = 0
for z in zeros:
    next = [z]
    for k in range(1,10):
        new_next = []
        for i,j in next:
            #print(next, k)
            new_next += find_next(i,j,k)
        next = new_next
    counter += len(next)

print(counter)