# A PART
with open("12.txt") as f:
    text = f.read()
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
                #print(letter, len(actuals), fences)
                counter += len(actuals) * fences
                for i1, j1 in actuals:
                    c[i1][j1] = '.'
print(counter)

# B PART