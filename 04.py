# A PART
with open("04.txt") as f:
    text = f.read()
counter = 0
c = text.split('\n')
print(c)

def prestej_xmas(i,j,a):
    my_sum=0
    if a=='X':
        try:
            if c[i][j] + c[i][j+1] + c[i][j+2] + c[i][j+3] == 'XMAS':
                my_sum+=1
        except:
            pass
        try:
            if c[i][j] + c[i][j-1] + c[i][j-2] + c[i][j-3] == 'XMAS' and j-3 >= 0:
                my_sum+=1
        except:
            pass
        try:
            if c[i][j] + c[i+1][j] + c[i+2][j] + c[i+3][j] == 'XMAS':
                my_sum+=1
        except:
            pass
        try:
            if c[i][j] + c[i-1][j] + c[i-2][j] + c[i-3][j] == 'XMAS' and i-3 >= 0:
                my_sum+=1
        except:
            pass
        try:
            if c[i][j] + c[i+1][j+1] + c[i+2][j+2] + c[i+3][j+3] == 'XMAS':
                my_sum+=1
        except:
            pass
        try:
            if c[i][j] + c[i+1][j-1] + c[i+2][j-2] + c[i+3][j-3] == 'XMAS' and j-3 >= 0:
                my_sum+=1
        except:
            pass
        try:
            if c[i][j] + c[i-1][j+1] + c[i-2][j+2] + c[i-3][j+3] == 'XMAS' and i-3 >= 0:
                my_sum+=1
        except:
            pass
        try:
            if c[i][j] + c[i-1][j-1] + c[i-2][j-2] + c[i-3][j-3] == 'XMAS' and i-3 >= 0 and j-3 >= 0:
                my_sum+=1
        except:
            pass
    return my_sum
        

for i, row in enumerate(c):
    for j, a in enumerate(row):
        counter += prestej_xmas(i,j,a)
print(counter)

counter = 0

def prestej_x_mas(i,j,a):
    if a == 'A':
        try:
            niz1 = c[i-1][j-1] + c[i+1][j+1]
            niz2 = c[i-1][j+1] + c[i+1][j-1]
            niz1 = ''.join(sorted(niz1))
            niz2 = ''.join(sorted(niz2))
        except:
            niz1 = 'MM'
            niz2 = 'MM'
        if i!=0 and j!=0 and niz1 == 'MS' and niz2 == 'MS':
            return 1
        else:
            return 0
    else:
        return 0

for i, row in enumerate(c):
    for j, a in enumerate(row):
        counter += prestej_x_mas(i,j,a)
print(counter)