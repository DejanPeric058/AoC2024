# A PART
import copy
with open("06.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
commands = [[a for a in command] for command in commands]
print(commands)

def find_pointer(map):
    for i, row in enumerate(map):
        for j, a in enumerate(row):
            if a in '<>V^':
                return i, j, a
            
def make_move(i,j,sign, map):
    map[i][j] = 'X'
    if sign == '<':
        if map[i][j-1] == '#':
            return make_move(i, j, '^', map)
        else:
            return i, j-1, '<', map
    elif sign == '^':
        if map[i-1][j] == '#':
            return make_move(i, j, '>', map)
        else:
            return i-1, j, '^', map
    elif sign == '>':
        if map[i][j+1] == '#':
            return make_move(i, j, 'V', map)
        else:
            return i, j+1, '>', map
    elif sign == 'V':
        if map[i+1][j] == '#':
            return make_move(i, j, '<', map)
        else:
            return i+1, j, 'V', map

def preveri_rob(i,j,sign):
    if sign=='V' and i == len(commands)-1:
        return False
    elif sign == '<' and j == 0:
        return False
    elif sign == '>' and j == len(commands[0])-1:
        return False
    elif sign=='^' and i == 0:
        return False
    else:
        return True


i, j, sign = find_pointer(commands)
map = copy.deepcopy(commands)
while preveri_rob(i,j,sign):
    i,j,sign,map = make_move(i,j,sign,map)
map[i][j] = 'X'
for row in map:
    counter += row.count('X')

print(counter)
# B PART

i1, j1, sign1 = find_pointer(commands)
potentials = []
for i, row in enumerate(map):
    for j, a in enumerate(row):
        if a == 'X'  and (i,j) != (i1,j1):            
            potentials.append((i,j))

counter = 0
print(len(potentials), len(commands) * len(commands[0]))
for a, b in potentials:
    #print(a,b)
    #print(b)
    map = copy.deepcopy(commands)
    map[a][b] = '#'
    #print(map==commands)
    i, j, sign = find_pointer(commands)
    combinations = {str(i) + ',' + str(j) + ',' + sign}
    niz = ''
    c = 0
    while preveri_rob(i,j,sign):
        #print(combinations)
        i,j,sign,map = make_move(i,j,sign,map)
        #print(str(i) + ',' + str(j) + ',' + sign)
        if str(i) + ',' + str(j) + ',' + sign in combinations:
            counter += 1
            # niz = ''
            # map[a][b] = '0'
            # for row in map:
            #     for a in row:
            #         niz += a 
            #     niz +='\n'
            # print(niz)
            break
        else:
            combinations.add(str(i) + ',' + str(j) + ',' + sign)
            #c += 1
print(counter)