# A PART
with open("07.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
new_commands = []
for c in commands:
    test, numbers = c.split(': ')
    numbers = [int(a) for a in numbers.split()]
    new_commands.append([int(test),numbers])

def numConcat(num1, num2):
 
     # find number of digits in num2
     digits = len(str(num2))
 
     # add zeroes to the end of num1
     num1 = num1 * (10**digits)
 
     # add num2 to num1
     num1 += num2
 
     return num1

def binary_combinations(n):
    sez = []
    # Loop through all numbers from 0 to 2^n - 1
    for i in range(1 << n):
        # Convert the current number to a binary string of length n
        binary_str = format(i, '0' + str(n) + 'b')
        sez.append(binary_str)
    return sez

def ternary_combinations(n):
    sez = []
    # Loop through all numbers from 0 to 3^n - 1
    for i in range(3**n):
        # Convert the current number to a ternary string of length n
        ternary_str = ''
        temp = i
        for _ in range(n):
            ternary_str = str(temp % 3) + ternary_str
            temp //= 3
        # Pad with zeros if needed
        ternary_str = ternary_str.zfill(n)
        sez.append(ternary_str)
    return sez

for test, numbers in new_commands:
    bits = ternary_combinations(len(numbers)-1)
    for b in bits:
        result = numbers[0]
        for i, d in zip([e for e in b],numbers[1:]):
            if i == '1':
                result += d
            elif i == '0':
                result = numConcat(result,d)
            else:
                result *= d
        if result == test:
            #print(test,numbers)
            counter += test
            break
print(counter)