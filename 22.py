# A PART
with open("22.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
commands = [int(a) for a in commands]
#print(commands)
# 16777216 je 2**24
for a in commands:
    for _ in range(2000):
        a = ((a << 6) ^ a) % 16777216
        a = ((a >> 5) ^ a) % 16777216
        a = ((a << 11) ^ a) % 16777216
    counter += a
print(counter)