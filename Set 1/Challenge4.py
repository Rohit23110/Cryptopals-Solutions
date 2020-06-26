"""The task in this challenge is to read the encrypted hex strings from a file and detect
which string has been encrypted using single byte XOR cipher. To do this, I reused my code
from the previous challenge. All the strings are decrypted using brute force and a list of 
best possible plain text messages for each string is returned. The best possible candidate 
in this list is most likely to have been encrypted using single byte XOR cipher and the
corresponding decrypted message is printed.""" 

from Challenge3 import singleByteXOR, calculateScore, convertBytesToString, decryptMessage

def readFile(fileName):
    """This function reads from the given file and returns a list of encrypted hex messages"""

    textFile = open(fileName, 'r')
    encryptedMessages = []
    for line in textFile:
        encryptedMessages.append(line.rstrip())
    textFile.close()
    return encryptedMessages

def findBestPossibleCandidate(encryptedMessages):
    """This function decrypts all the encrypted messages using appropriate keys and finds 
    the best possible message encrypted using single byte XOR cipher"""

    candidatesForSingleByteXOR = []
    for encryptedMessage in encryptedMessages:
        decryptedMessage = decryptMessage(encryptedMessage)[0] # Only the most likely message is stored
        # The below check cannot be used as the correct output consists of line feed which is not a printable character. This leads to the wrong answer.
        # messageString = convertBytesToString(message[0]) 
        # if messageString.isprintable(): 
        decryptedMessage["encryptedMessage"] = encryptedMessage
        candidatesForSingleByteXOR.append(decryptedMessage)
    candidatesForSingleByteXOR.sort(key = lambda x:x["score"])
    return candidatesForSingleByteXOR[0]

def printMessage(message):
    print("Most likely encrypted message - " + message["encryptedMessage"])
    print("Corresponding decrypted message - " + convertBytesToString(message["messageInBytes"]).rstrip())
    print("Score - " + "{0:.2f}".format(message["score"]))
    print("Key - " + message["key"])

if __name__ == "__main__":
    encryptedMessages = readFile('Challenge4.txt')
    bestCandidate = findBestPossibleCandidate(encryptedMessages)
    printMessage(bestCandidate)