# The task is to write a function that takes two equal-length buffers and produces their XOR combination.
# Input String 1 - 1c0111001f010100061a024b53535009181c
# Input String 2 - 686974207468652062756c6c277320657965
# Expected Output - 746865206b696420646f6e277420706c6179

# This function performs XOR operation on two string and returns the output
def fixedXOR(hexString1, hexString2):
    intNumber1 = int(hexString1, 16)
    intNumber2 = int(hexString2, 16)
    hexOutput = hex(intNumber1 ^ intNumber2)[2:]
    return hexOutput

hexString1 = input("Enter the hex string 1 - ")
hexString2 = input("Enter the hex string 2 - ")
hexOutput = fixedXOR(hexString1, hexString2)
print("XOR of both strings is - " + hexOutput)