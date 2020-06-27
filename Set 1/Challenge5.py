"""
The task in this challenge is to create a function which performs repeating key 
XOR encryption. 
Input - Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal
Key - ICE
Expected Output - 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a2622632
4272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
"""

def repeatingKeyXOR(byteString, byteKey):
    """This function XORs the given byte string with the byte key using repeating key XOR 
    technique. It can be used for encryption and decryption."""

    outputMessage = b""
    lengthOfKey = len(byteKey)
    for i in range(len(byteString)):
       outputMessage += (byteString[i] ^ byteKey[i % lengthOfKey]).to_bytes(1, "big")
    return outputMessage 

def inputMessage():
    """This function is used for taking multi-line input. This challenge gives us two 
    strings as input which are separated by a newline character. This cannot be received 
    using the in-built input function. Hence, a custom function is created""" 
    
    print("Enter the message to be encrypted, Press Enter to add a new line or Press Ctrl-Z to stop:")
    message = ""
    while True:
        try:
            line = input()
        except EOFError:
            break
        message += "\n" + line
    return message.lstrip()


if __name__ == "__main__":
    message = inputMessage()
    key = input("\nEnter the key for encryption - ")
    encryptedMessage = repeatingKeyXOR(str.encode(message), str.encode(key))
    print("\nEncrypted message - " + encryptedMessage.hex())

    # This verifies if we get the expected output for given input. Not needed if used for other inputs.
    # assert encryptedMessage.hex() == '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f', "Encrypted message is not same as expected output"