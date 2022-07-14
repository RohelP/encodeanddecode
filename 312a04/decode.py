compressed = []
toexp = open("decoded.txt", "w")
with open('compressed.bin', 'rb')as fileinput:
   for line in fileinput:
    for char in line:
        arr = []
        num = int(char)
        for x in range(8):
            arr.append(num%2)
            num = num >> 1
        arr.reverse()
        compressed+= arr
        

    ret = ''
    cur_node = huffman_tree
    for char in strg:
        cur_node = cur_node[int(char)]
        if cur_node is None:
            raise ValueError
        elif isinstance(cur_node, str):
            ret += cur_node
            cur_node = huffman_tree        

