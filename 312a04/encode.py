import heapq


version = 0
encodableChar = " ,.0123456789abcdefghijklmnopqrstuvwxyz"
freqTable = {}
for char in encodableChar:
    freqTable[char] = 0
with open('test1.txt', 'r') as fileinput:
    for line in fileinput:
        line = line.lower()
        for char in line:
            if char.isspace():
                freqTable[" "] += 1
            elif char.isalnum() or char == "." or char ==",":
                freqTable[char] += 1
f = open("frequency.txt", "w")
for key in freqTable:
    if key == "z":
        f.write(key+":"+str(freqTable[key]))
    else:
        f.write(key+":"+str(freqTable[key])+"\n")
f.close()


class NodeTree():
    def __init__(self, char, left=None, right=None):
        global version
        self.version = version
        version+=1
        self.left = left
        self.right = right
        self.char = char
    def __lt__(self,other):
        return self.version < other.version
        
keys = []
for key in freqTable:
    # if freqTable[key] != 0:
    keys.append((freqTable[key],NodeTree(key)))
heapq.heapify(keys)
# x = heapq.heappop(keys)
# x2 = heapq.heappop(keys)
# print(x[0]+x2[0])
while len(keys) != 1:
    x = heapq.heappop(keys)
    x2 = heapq.heappop(keys)
    heapq.heappush(keys,(x[0]+x2[0],NodeTree(None,x[1],x2[1])))
res = []
def dfs(tree):
    if tree.char !=  None:
        print(tree.char+":"+"".join(res))
    else:
        res.append("0")
        dfs(tree.left)
        res.pop()
        res.append("1")
        dfs(tree.right)
        res.pop()
dfs(keys[0][1])