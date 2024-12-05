# A PART
with open("05.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
part1 = {}
part2 = []
flag = True
for c in commands:
    if c == '':
        flag = False
    elif flag == True:
        a, b = c.split('|')[0], c.split('|')[1]
        try:
            part1[a].append(b)
        except:
            part1[a] = [b]
    else:
        part2.append(c.split(','))
def correct(row,a,part1):
    try:
        for b in part1[a]:
            if b in row and row.index(a) > row.index(b):
                return False
        return True
    except:
        return True

for row in part2:
    flag = True
    for a in row:
        if not correct(row, a, part1):
            flag = False
    if flag == True:
        counter += int(row[len(row)//2])

print(counter)

# B PART
counter = 0 

def get_new_row(row, part1):
    new_row = row.copy()
    for a in row:
        if a in part1.keys():
            for b in part1[a]:
                if b in row:
                    i1, i2 = new_row.index(a), new_row.index(b)
                    if i1 > i2:
                        new_row[i1], new_row[i2] = b, a
    return new_row

def is_ordered(row, part1):
    flag = True
    for a in row:
        if not correct(row, a, part1):
            flag = False
    return flag

for row in part2:
    new_row = row.copy()
    while not is_ordered(new_row, part1):
        new_row = get_new_row(new_row, part1)
    if new_row != row:
        counter += int(new_row[len(new_row)//2])

print(counter)

# Med 6310, 6311, 6313, 6314