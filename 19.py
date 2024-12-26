# A PART
with open("19.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
towels = commands[0].split(', ')
designs = commands[2:]
#print(len(towels))
#towels = set(towels)

def foo(s):
    global towels
    if not s:
        return True
    for sub in towels:
        if s[-len(sub):] == sub:
            if foo(s[:-len(sub)]):
                return True
    return False

for d in designs:
    if foo(d):
        counter += 1
print(counter)

# B PART

counter = 0
# Trie data structure
class Trie:
	def __init__(self):
		self.endOfWord = False
		self.children = [None]*26

# Inserting the strings into trie
def insert(root, s):
	n = len(s)
	prev = root
	for i in range(n):
		index = ord(s[i]) - ord('a')
		if prev.children[index] is None:
			prev.children[index] = Trie()
		prev = prev.children[index]
	prev.endOfWord = True

# Function to find number of ways
# of forming string str
def waysOfFormingString(root, s):
	n = len(s)

	# Count[] to store the answer
	# of prefix string str[0....i]
	count = [0]*n
	for i in range(n):
		ptr = root
		for j in range(i, -1, -1):
			ch = s[j]

			# If not found, break
			# out from loop
			index = ord(ch) - ord('a')
			if ptr.children[index] is None:
				break
			ptr = ptr.children[index]

			# String found, update the
			# count(i)
			if ptr.endOfWord:
				if j > 0:
					count[i] += count[j - 1]
				else:
					count[i] += 1
	return count[n - 1]

# Driver code

	
m = len(towels)
# Construct trie
for d in designs:
    root = Trie()
    for i in range(m):
        insert(root, towels[i][::-1])
        # Function call
    #print(waysOfFormingString(root, d))
    counter += waysOfFormingString(root, d)
print(counter)