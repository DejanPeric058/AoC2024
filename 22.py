# A PART
with open("22.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
commands = [int(a) for a in commands]
#print(commands)
# 16777216 je 2**24
sequences = []
# for a in commands:
#     for _ in range(2000):
#         a = ((a << 6) ^ a) % 16777216
#         a = ((a >> 5) ^ a) % 16777216
#         a = ((a << 11) ^ a) % 16777216
#     counter += a
# print(counter)

# B PART

counter = 0
def find_first_seq(seq, derivatives, sequences):
    # k = derivatives.index(seq)
    # if k == -1:
    #     return 0
    # else:
    #     return sequences[k//2 + 4]
    try:
        k = derivatives.index(seq)
        return sequences[k//2 + 4]
    except:
        return 0

sez = []
b = 0
for a in commands:
    derivatives = ''
    b = a % 10
    sequences = [b]
    for _ in range(2000):
        a = ((a << 6) ^ a) % 16777216
        a = ((a >> 5) ^ a) % 16777216
        a = ((a << 11) ^ a) % 16777216

        if a % 10 - b >= 0:
            derivatives += '+'
            derivatives += str(a % 10 - b)
        else:            
            derivatives += str(a % 10 - b)
        b = a % 10
        sequences.append(b)
    #print(sequences,derivatives)
    sez.append((sequences,derivatives))

def help(num):
    if num >= 0:
        return '+' + str(num)
    else:
        return str(num)

combinations = []
for x1 in range(-9,10):
    for x2 in range(-9,10):
        for x3 in range(-9,10):
            for x4 in range(-9,10):
                word = help(x1)+help(x2)+help(x3)+help(x4)
                combinations.append(word)
print(len(combinations))

for c in combinations:
    new_counter = 0
    for s, d in sez:
        #print(find_first_seq('-2+1-1+3',d,s))
        new_counter += find_first_seq(c,d,s)
    counter = max(counter,new_counter)
print(counter)