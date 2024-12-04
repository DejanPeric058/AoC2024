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


#aaaa