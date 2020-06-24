# The challenge is to break a string encrypted using single byte XOR cipher and return the decrypted message
# Input - 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# In this version, the user can view the 5 most probable decryted messages
# Frequency analysis of each decryted message is done to give us a score.
# The top 5 messages with the best scores are displayed.

# This function XORs the entire encrypted message with a character string, created by repeating the hex 
# representation of the character parameter, to give us the decrypted message.
def singleByteXOR(hexString, character): 
    if len(character[2:]) == 1:
    # If the hex representation of a number is a single digit then a zero has to appended so as to make each hex number 2 digits. 
        characterString = ("0" + character[2:]) * (len(hexString) // 2) 
    else:
        characterString = character[2:] * (len(hexString) // 2)
    intCharacter = int(characterString, 16) 
    intNumber = int(hexString, 16)
    xoredHex = hex(intNumber ^ intCharacter)[2:]
    if len(xoredHex) < len(hexString):
        xoredHex = ("0" * (len(hexString) - len(xoredHex))) + xoredHex # This has to be done as there can be as many zeroes as many 
        # characters match with the hex string. Python strips the zeroes at the start of a XORed string which have to be added again.
    return xoredHex

# This function calculates the score for a given decrypted message. The score is calculated as the sum of the weights of
# each letter in the decrypted message. The assumption is that the message having the best score has the highest 
# probability of being the actual message. 
def calculateScore(decryptedMessage):
    # This dictionary contains the weights of each letter. These weights are calculated by analyzing the frequency of 
    # each letter in common words. Source - http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    frequencyDictionary = { 
        "A": 8.12, "B": 1.49, "C": 2.71, "D": 4.32, "E": 12.02,
        "F": 2.30, "G": 2.03, "H": 5.92, "I": 7.31, "J": 0.10,
        "K": 0.69, "L": 3.98, "M": 2.61, "N": 6.95, "O": 7.68,
        "P": 1.82, "Q": 0.11, "R": 6.02, "S": 6.28, "T": 9.10,
        "U": 2.88, "V": 1.11, "W": 2.09, "X": 0.17, "Y": 2.11,
        "Z": 0.07
    } 

    score = 0
    for i in range(len(decryptedMessage)):
        decimalRep = ord(decryptedMessage[i])
        if (decimalRep > 96 and decimalRep < 123) or (decimalRep > 64 and decimalRep < 91):
            score += frequencyDictionary[decryptedMessage[i].upper()]

    return score

# This function solve the problem faced by using bytes.decode and printing unprintable characters.
# It converts each pair of hexadecimal digits using the function chr(). If the character is not 
# printable, then it is stored in the string as '\xAB'. where AB represent the 2 hex digits.
def convertHexToString(hexString):
    characterString = ""
    for i in range(0, len(hexString), 2):
        characterString += chr(int(hexString[i: i + 2], 16))
    return characterString

# This functions decrypts the hexString using all 256 possible combinations of characters and 
# return a list of the best possible 5 messages. The expected output (Cooking MC's like a pound
# of bacon) appears as the 5th possible message using this code.
def decryptMessage(hexString):
    messageList = []
    for i in range(256):
        xoredHex = singleByteXOR(hexString, hex(i))
        decryptedMessage = convertHexToString(xoredHex)
        score = calculateScore(decryptedMessage)
        if not messageList:
            messageList.append([decryptedMessage, score])
        else:
            for message in messageList:
                if score > message[1]:
                    messageList.insert(messageList.index(message), [decryptedMessage, score])
                    break
            if len(messageList) > 5:
                messageList.pop()
    return messageList

hexString = input("Enter the hex string - ")
print("\nList of most probable decrypted strings is - ")
messageList = decryptMessage(hexString)

for i in range(5):
    print(str(i + 1) + ") Message - " + messageList[i][0] + " Score - " + str(messageList[i][1]))

