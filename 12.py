import copy
# A PART
with open("12.txt") as f:
    text = f.read()
# counter = 0
# commands = text.split('\n')
# commands = [[a for a in command] for command in commands]
# letters = set()
# N, M = len(commands), len(commands[0])
# c = [['.' for _ in range(M+2)]]
# c += [['.'] + [a for a in row] + ['.'] for row in commands]
# c += [['.' for _ in range(M+2)]]
# for row in c:
#     for a in row:
#         if a != '.':
#             letters.add(a)
# print(letters)

# for letter in letters:
#     for i, row in enumerate(c):
#         for j, a in enumerate(row):
#             if a == letter:
#                 c[i][j] = '#'
#                 actuals = [(i,j)]
#                 potentials = [(i,j)]
#                 fences = 0
#                 while len(potentials) > 0:
#                     new_potentials = []
#                     for i1, j1 in potentials:
#                         if c[i1-1][j1] == letter:
#                             c[i1-1][j1] = '#'
#                             new_potentials.append((i1-1,j1))
#                             actuals.append((i1-1,j1))
#                         elif c[i1-1][j1] != '#':
#                             fences += 1
#                         if c[i1+1][j1] == letter:
#                             c[i1+1][j1] = '#'
#                             new_potentials.append((i1+1,j1))
#                             actuals.append((i1+1,j1))
#                         elif c[i1+1][j1] != '#':
#                             fences += 1
#                         if c[i1][j1-1] == letter:
#                             c[i1][j1-1] = '#'
#                             new_potentials.append((i1,j1-1))
#                             actuals.append((i1,j1-1))
#                         elif c[i1][j1-1] != '#':
#                             fences += 1
#                         if c[i1][j1+1] == letter:
#                             c[i1][j1+1] = '#'
#                             new_potentials.append((i1,j1+1))
#                             actuals.append((i1,j1+1))
#                         elif c[i1][j1+1] != '#':
#                             fences += 1
#                     potentials = new_potentials
#                 #print(letter, len(actuals), fences)
#                 counter += len(actuals) * fences
#                 for i1, j1 in actuals:
#                     c[i1][j1] = '.'
# print(counter)

# B PART


counter = 0
commands = text.split('\n')
commands = [[a for a in command] for command in commands]
letters = set()
N, M = len(commands), len(commands[0])
c = [['.' for _ in range(M+2)]]
c += [['.'] + [a for a in row] + ['.'] for row in commands]
c += [['.' for _ in range(M+2)]]
for row in c:
    for a in row:
        if a != '.':
            letters.add(a)
print(letters)

def subtract_fences(h1):
    h = copy.deepcopy(h1)
    num = 0
    for i, row in enumerate(h):
        for j, k in enumerate(row):
            if k != '#':
                h[i][j] = '-'
    #print(h)
    for i in range(N+1):
        for j in range(M+1):
            alpha, beta, gamma, delta = h[i][j], h[i][j+1], h[i+1][j], h[i+1][j+1]
            if alpha == beta and gamma == delta and alpha != gamma:
                num += 1
            elif alpha != beta and beta == delta and alpha == gamma:
                num += 1
    return num
 
for letter in letters:
    for i, row in enumerate(c):
        for j, a in enumerate(row):
            if a == letter:
                c[i][j] = '#'
                actuals = [(i,j)]
                potentials = [(i,j)]
                fences = 0
                while len(potentials) > 0:
                    new_potentials = []
                    for i1, j1 in potentials:
                        if c[i1-1][j1] == letter:
                            c[i1-1][j1] = '#'
                            new_potentials.append((i1-1,j1))
                            actuals.append((i1-1,j1))
                        elif c[i1-1][j1] != '#':
                            fences += 1
                        if c[i1+1][j1] == letter:
                            c[i1+1][j1] = '#'
                            new_potentials.append((i1+1,j1))
                            actuals.append((i1+1,j1))
                        elif c[i1+1][j1] != '#':
                            fences += 1
                        if c[i1][j1-1] == letter:
                            c[i1][j1-1] = '#'
                            new_potentials.append((i1,j1-1))
                            actuals.append((i1,j1-1))
                        elif c[i1][j1-1] != '#':
                            fences += 1
                        if c[i1][j1+1] == letter:
                            c[i1][j1+1] = '#'
                            new_potentials.append((i1,j1+1))
                            actuals.append((i1,j1+1))
                        elif c[i1][j1+1] != '#':
                            fences += 1
                    potentials = new_potentials
                fences -= subtract_fences(c)
                #print(c)
                #print(letter, len(actuals), fences)
                counter += len(actuals) * fences
                for i1, j1 in actuals:
                    c[i1][j1] = '.'
print(counter)