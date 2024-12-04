# A PART
import re

with open("03.txt") as f:
    text = f.read()
counter = 0
x = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|don\'t\(\)|do\(\)",text)
status = True
for a in x:
    if a[0] == 'm' and status == True:
        alpha, beta = a[4:-1].split(',')
        counter += int(alpha)*int(beta)
    elif a == "don\'t()":
        status=False
    elif a == "do()":
        status=True
    
print(counter)
