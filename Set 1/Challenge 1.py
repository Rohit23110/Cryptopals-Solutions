# The task is to convert the given hex string to base64
# Input - 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Expected Output - SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

import base64

def hexToBase64(hexString):
    base64Number = base64.encodebytes(bytes.fromhex(hexString)) # It first converts the hex string into raw bytes and then encodes the bytes to base 64.
    return bytes.decode(base64Number, "UTF-8") # The base 64 bytes are encoded using UTF-8 and the resulting string is returned

hexString = input("Enter the hex string - ")
print("Converting the hex bytes to characters - " + bytes.decode(bytes.fromhex(hexString), "UTF-8"))
base64String = hexToBase64(hexString)
print("Converting hex to Base 64 - " + base64String)