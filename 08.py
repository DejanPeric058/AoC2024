# A PART
with open("08.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
commands = [[b for b in c] for c in commands]
my_dict = {}
for i, row in enumerate(commands):
    for j, a in enumerate(row):
        if a != '.':
            try:
                my_dict[a].append((i,j))
            except:
                my_dict[a] = [(i,j)]
niz = ''
for c in commands:
    for b in c:
        niz += b
    niz += '\n'
#print(niz)
#print(my_dict)
for sez in my_dict.values():
    for i, (x1, y1) in enumerate(sez):
        for x2, y2 in sez[i+1:]:
            x, y = x2 - x1, y2 - y1
            
            
            k=0
            for k in range(10000):
                x3, y3 = x1 - k*x, y1 - k*y
                try:
                    if x3 >= 0 and y3 >= 0:
                        commands[x3][y3] = '#'
                except:
                    break
            k=0
            for k in range(10000):
                x4, y4 = x2 + k*x, y2 + k*y
                try:
                    if x4 >= 0 and y4 >= 0:
                        commands[x4][y4] = '#'
                except:
                    break
            

niz = ''
for c in commands:
    for b in c:
        if b == '#':
            counter += 1
        niz += b
    niz += '\n'
print(counter)
            
