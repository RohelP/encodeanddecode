import heapq

givenstring = " ,.0123456789abcdefghijklmnopqrstuvwxyz"
tab = {}

for char in givenstring:
    tab[char] = 0
with open('test1.txt', 'r') as fileinput:
    for line in fileinput:
        line = line.lower()
        for char in line:
            if char.isspace():
                tab[" "] += 1
            elif char.isalnum() or char == "." or char ==",":
                tab[char] += 1

f = open("frequency.txt", "w")
for key in tab:
    if key == "z":
        f.write(key+":"+str(tab[key]))
    else:
        f.write(key+":"+str(tab[key])+"\n")
f.close()


class NodeTree():

    def __init__(self, left=None, right=None):
        self.right = right
        self.left = left

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
for (char, frequency) in freq:
    if char == freq[-1][0]:
        f.write(char + ":" + huffmanCode[char])
    else:
        f.write(char + ":" + huffmanCode[char] + '\n')

f.close()