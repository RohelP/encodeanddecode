'''
Rohel Pereira
200668360
'''


givenstring = " ,.0123456789abcdefghijklmnopqrstuvwxyz"
tab = {}
arr = []

class NodeTree():

    def __init__(self, left=None, right=None):
        self.right = right
        self.left = left

for sym in givenstring:
    tab[sym] = 0

with open('test1.txt', 'r') as fileinput:
    for line in fileinput:
        line = line.lower()

        for sym in line:
            if sym.isspace():
                tab[" "] += 1
            elif sym.isalnum() or sym == "." or sym ==",":
                tab[sym] += 1

f = open("frequency.txt", "w")
for x in tab:
    if x == "z":
        f.write(x+":"+str(tab[x]))
    else:
        f.write(x+":"+str(tab[x])+"\n")

f.close()

def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}

    dictionary = dict()
    l = node.left
    r = node.right 

    huff = huffman_code_tree(l, True, binString + '1')
    dictionary.update(huff)
    huff = huffman_code_tree(r, False, binString + '0')
    dictionary.update(huff)
    
    return dictionary


freq = sorted(tab.items(), key=lambda x: x[1], reverse=True)
link = freq

while len(link) > 1:
    key1, c1 = link[-1]
    key2, c2 = link[-2]
    link = link[:-2]
    node = NodeTree(key1, key2)
    link.append((node, c1 + c2))

    link = sorted(link, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(link[0][0])

f = open("codes.txt", "w")
for (sym, frequency) in freq:
    if sym == freq[-1][0]:
        f.write(sym + ":" + huffmanCode[sym])
    else:
        f.write(sym + ":" + huffmanCode[sym] + '\n')

f.close()

d = open("compressed.bin", "wb")
with open('test1.txt', 'r') as fileinput:
    for loop in fileinput:
        loop = loop.lower()
        for num in loop:
            if num in huffmanCode:
                arr += huffmanCode[num]
        
bins="".join(map(str,arr))
byt = bytearray(int(bins[count:count+8], 2) 

for count in range(0, len(bins), 8))
d.write(byt)

d.close()
