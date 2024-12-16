# A PART
import numpy as np
with open("13.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n\n')
equi = []
for c in commands:
    d = c.split('\n')
    e1 =d[0].replace('Button A: X+', '').replace(' Y+','').split(',')
    e2 =d[1].replace('Button B: X+', '').replace(' Y+','').split(',')
    e3 =d[2].replace('Prize: X=', '').replace(' Y=','').split(',')
    a = np.array([[int(e1[0]),int(e2[0])],[int(e1[1]),int(e2[1])]])
    b = np.array([10000000000000+int(e3[0]), 10000000000000+int(e3[1])])
    equi.append((a,b))
#print(equi)
# for a,b in equi:
#     x = np.linalg.solve(a,b)
#     #print(x[0] - int(x[0]), x[1])
#     if round(x[0],5).is_integer() and round(x[1],5).is_integer():#abs(x[0] - int(x[0])) < 10**(-2) and abs(x[1] - int(x[1])) < 10**(-2):
#         counter += int((round(x[0],5)))*3 + int(round(x[1],5)*1)
#     else:
#         print(a,b,x)
#         print(x[0], x[1])
for a,b in equi:
    x0 = (b[0]*a[1][1]-b[1]*a[0][1])/(a[0][0]*a[1][1]-a[0][1]*a[1][0])
    x1 = (b[1]*a[0][0]-b[0]*a[1][0])/(a[0][0]*a[1][1]-a[0][1]*a[1][0])
    #print(x[0] - int(x[0]), x[1])
    if x0.is_integer() and x1.is_integer():
        counter += x0*3 + x1
    # else:
    #     print(a,b,x)
    #     print(x[0], x[1])
print(counter)