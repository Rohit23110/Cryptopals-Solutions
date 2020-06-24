# The challenge is to break a string encrypted using single byte xor cipher and return the decrypted message
# Input - 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# In this version, the user has to manually check the 256 possible combinations and find the correct message
# As only 1 of the messages makes sense (Cooking MC's like a pound of bacon), it is easy to find it.
# This code works only upto 128 characters and stops working for character 129 as bytes.decode cannot process the character "0x9b".

def singleByteXOR(hexString, character):
    output = ""
    for i in range(0, len(hexString), 2):
        intNumber = int(hexString[i : i + 2], 16)
        intCharacter = int(character, 16)
        xoredHex = hex(intNumber ^ intCharacter)[2:]
        if len(xoredHex) < 2:
            xoredHex = "0" + xoredHex
        output += xoredHex
    return output

hexString = input("Enter the hex string - ")
for i in range(256):
    print("Character used - " + chr(i) + "Decrypted string is - " + bytes.decode(bytes.fromhex(singleByteXOR(hexString, hex(i))), "UTF-8"))