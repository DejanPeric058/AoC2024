from collections import deque

# A PART
with open("09.txt") as f:
    text = f.read()
# counter = 0
# #print(text)
# de = deque([])
# for i, a in enumerate(text):
#     if i%2==0:
#         b = str(i//2)
#     else:
#         b = '.'
#     de.extend([b for _ in range(int(a))])
    
# #print(de)
# start = 0
# end = len(de)
# while '.' in de:
#     c = de.pop()
#     if c != '.':
#         loc = de.index('.',start,end)
#         de[loc] = c
#         start = loc
# #print(de)
# for i, d in enumerate(de):
#     counter += i*int(d)
# print(counter)
counter = 0
#print(text)
number_dict = {}
empty_dict = {}
end = len(text)
start = 0
for i, a in enumerate(text):
    if i%2==0:
        number_dict[i//2] = (start,start + int(a))
    else:
        empty_dict[end + i//2] = (start,start + int(a))
    start += int(a)

#print(number_dict, empty_dict)
for key, (start, end) in sorted(list(number_dict.items()), reverse=True):
    s, e, k = -1, -1, -1
    #print ("Checking {0} in {1} {2}".format(key, start, end))
    for key1, (start1, end1) in sorted(list(empty_dict.items()), reverse=False):
        razlika, razlika1 =  end - start, end1 - start1
        if start1 > start:
            break
        elif razlika <= razlika1:
            number_dict[key] = (start1, start1 + razlika)
            empty_dict[key1] = (start1 + razlika, end1)
            break

#print(number_dict, empty_dict)
for key, (start, end) in sorted(list(number_dict.items()), reverse=True):
    for z in range(start, end):
        counter += key*z
print(counter)