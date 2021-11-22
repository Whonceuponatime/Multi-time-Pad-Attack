def myXOR(x, y):
    res = 0 # Initialize result
 
    # Assuming 32-bit Integer
    for i in range(31, -1, -1):
         
        # Find current bits in x and y
        b1 = x & (1 << i)
        b2 = y & (1 << i)
        b1 = min(b1, 1)
        b2 = min(b2, 1)
 
        # If both are 1 then 0
        # else xor is same as OR
        xoredBit = 0
        if (b1 & b2):
            xoredBit = 0
        else:
            xoredBit = (b1 | b2)
 
        # Update result
        res <<= 1;
        res |= xoredBit
    return res
col1 = ["6a", "79", "6f", "65", "65", "63", "69"]
c1 = []
character = ord("v")
for i in range(0, len(col1)):
    c1.append(int(col1[i], 16))
key = (myXOR(c1[0], character))

for i in range(1, len(c1)):

    print(col1[i], chr(character), key, chr(myXOR(c1[i], key)))
