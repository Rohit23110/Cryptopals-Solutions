import binascii

"""The challenge is to break a string encrypted using single byte XOR cipher and return the decrypted message
Input - 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
In this version, the user can view the 5 most probable decryted messages
Frequency analysis of each decrypted message is done to give us a score.
The message with best score is printed. This code works assuming that the message consists of only spaces
and english letters. It will lead to wrong decryption if the message has unprintable/wierd characters."""

def singleByteXOR(hexString, character): 
    """This function XORs the entire encrypted message with a character string, created by repeating the hex 
    representation of the character parameter, to give us the bytes of decrypted message."""

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
    return bytes.fromhex(xoredHex)


def calculateScore(bytesString):
    """This function calculates the score for a given string of bytes. The function first finds the relative frequency of  
    each character represented by the byte in the text. Then the score is calculated as the average of absolute difference 
    between the frequencies of letters in the decrypted message and the corresponding letter in the English Language."""
    
    """This score represents the fitting quotient of the two frequency distributions. The closer the score is to 0 
    the better. This way of calculating a score is better than the naive method"""     

    frequencyDictionary = { # This dictionary contains the weights of each letter. These weights are calculated by analyzing the frequency of 
        # each letter in common words. This dictionary includes space as a character to give us better results.
        # Source - https://web.archive.org/web/20170918020907/http://www.data-compression.com/english.html
        " ": 19.18182, "A": 6.51738, "B": 1.24248, "C": 2.17339, "D": 3.49835, 
        "E": 10.41442, "F": 1.97881, "G": 1.58610, "H": 4.92888, "I": 5.58094,
        "J": 0.09033, "K": 0.50529, "L": 3.31490, "M": 2.02124, "N": 5.64513,
        "O": 5.96302, "P": 1.37645, "Q": 0.08606, "R": 4.97563, "S": 5.15760,
        "T": 7.29357, "U": 2.25134, "V": 0.82903, "W": 1.71272, "X": 0.13692,
        "Y": 1.45984, "Z": 0.07836
    }

    score = 0
    lengthOfString = len(bytesString)

    # The bytes string in stored as a list of integers so we can access/operate on it directly.
    frequencyList = [((bytesString.count(32) * 100) / lengthOfString)] # The formula has to be applied seperately for space as its ascii is not in range of the letters
    frequencyList = [((bytesString.count(i) * 100) / lengthOfString) + ((bytesString.count(i + 32) * 100) / lengthOfString) for i in range(65, 91)] + frequencyList
    score = (abs(frequencyList[26] - frequencyDictionary[" "]) + sum([abs(frequencyList[i] - frequencyDictionary[chr(i + 65)]) for i in range(26)])) / len(frequencyDictionary)

    return score


def convertBytesToString(byteString):
    """This function solve the problem faced by using bytes.decode and printing unprintable characters.
    It converts each byte using the function chr(). If the character is not printable, then it is stored 
    in the string as '\xAB'. where AB represent the 2 hex digits."""

    characterString = ""
    for num in byteString:
        characterString += chr(num)
    return characterString

def decryptMessage(hexString):
    """This function decrypts the hexString using all 256 possible combinations of characters and 
    return a list of the best possible 20 messages. The expected output (Cooking MC's like a pound
    of bacon) appears as the best possible message using this code."""

    messageList = []
    for i in range(256):
        bytesOfXoredHex = singleByteXOR(hexString, hex(i))
        score = calculateScore(bytesOfXoredHex)
        if not messageList:
            messageList.append([bytesOfXoredHex, score, chr(i)])
        else:
            for message in messageList:
                if score < message[1]:
                    messageList.insert(messageList.index(message), [bytesOfXoredHex, score, chr(i)])
                    break
            if len(messageList) > 20:
                messageList.pop()
    return messageList

def printMessage(messageList):
    """This function receives a list of messages, their scores and the key used to decrypt it. The list is
    arranged in ascending order of score, i.e. the best possible message is higher. If it is printable then
    that is the required message and it is printed, else it checks further down the list."""

    for message in messageList:
        messageString = convertBytesToString(message[0])
        if messageString.isprintable(): 
            print("Message - " + messageString + "   Score - " + "{:.2f}".format(message[1]) + "   Key - " + message[2])
            break

if __name__ == "__main__":
    hexString = input("Enter the hex string - ")
    print("\nThe most probable decrypted message is - ")
    messageList = decryptMessage(hexString)
    printMessage(messageList)
