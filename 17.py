import copy
# A PART
with open("17.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
A = int(commands[0].split(': ')[1])
B = int(commands[1].split(': ')[1])
C = int(commands[2].split(': ')[1])
program2 = commands[4].split(': ')[1]
# A, B, C = 2024, 2024, 43690
# program = '4,0'
program = program2.replace(',','')
program3 = program2.split(',')
program3.reverse()
program4 = copy.deepcopy(program3)
result = ''
pointer = 0
N = len(program)
print(A,B,C,program)



def op(operand):
    global A, B, C
    if operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    else:
        return operand

def operation(opcode, operand, pointer):
    global A, B, C, result, program4
    opcode, operand = int(opcode), int(operand)
    if opcode == 0:
        A = A >> op(operand)
        pointer += 2
    elif opcode == 1:
        B = B ^ operand
        pointer += 2
    elif opcode == 2:
        B = op(operand) % 8
        pointer += 2
    elif opcode == 3:
        if A == 0:
            pointer += 2
        else:
            pointer = operand
    elif opcode == 4:
        B = C ^ B
        pointer += 2 
    elif opcode == 5:
        r = str(op(operand) % 8)
        if True: #r == program4.pop():
            result += r
            result += ','
            pointer += 2
        else:
            pointer = 'NAPAKA'
    elif opcode == 6:
        B = A >> op(operand)
        pointer += 2
    elif opcode == 7:
        C = A >> op(operand)
        pointer += 2
    return pointer

initial = 14
flag = True
for _ in range(1):
#while flag:
    initial += 1 # pri 7ki je še 6ka, pri 5ki še 7ka
    A = 3*8**15 + 3*8**13 + 3*8**12 + 0*8**11+ 4*8**10 + 6*8**9 + 3*8**8 + 3*8**7 + 4*8**6 + 4*8**5 + 2*8**4 + 4*8**3 + 6*8**2 + 3*8**1 + 2
    print(A)
    program4 = copy.deepcopy(program3)
    pointer = 0
    result = ''
    while pointer < N-1:
        pointer = operation(program[pointer], program[pointer+1], pointer)
        # if pointer == 'NAPAKA':
        #     break
        # #print(A,B,C,result, pointer)
        # # print(pointer)
        # elif program4 == []:
        #     flag = False
        #print(result)
    
    print(program2,initial, 8**initial, result)
    print(program2[:6], result[:6])
    if result == program2 + ',':
        print(program2,initial, 8**initial, result)
        break





print(initial)

# B PART

