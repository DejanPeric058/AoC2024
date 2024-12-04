# A PART
with open("01.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
commands = [command.split() for command in commands]
prvi, drugi = [], []
for a, b in commands:
    prvi.append(int(a))
    drugi.append(int(b))
mysum = 0
prvi.sort()
drugi.sort()
for a, b in zip(prvi,drugi):
    mysum += abs(a-b)

print(mysum)

mysum2 = 0

for a in prvi:
    mysum2 += a*drugi.count(a)

print(mysum2)