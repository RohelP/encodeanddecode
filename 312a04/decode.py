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