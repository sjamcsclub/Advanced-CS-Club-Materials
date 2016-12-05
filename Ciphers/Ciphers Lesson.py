def sanitize(msg, key):
    return msg.upper(), key.upper()

def encrypt(encKey, message):
    newMsg= ""
    msg, key = sanitize(message, encKey)
    for i in range(len(msg)):
        if ord(msg[i]) == ord(" "):
            newMsg+=" "
        else:
            letterValue = ord(msg[i])
            shift = ord(key[i%len(key)])
            newLetterValue = chr((letterValue + shift)%26 +65)
            newMsg+=newLetterValue
    return newMsg

def decrypt(decKey, message):
    oldMsg = ""
    msg, key = sanitize(message, decKey)
    for i in range(len(msg)):
        if ord(msg[i]) == ord(" "):
            oldMsg+=" "

        else:
            letterValue = ord(msg[i])
            shift = ord(key[i%len(key)])
            newLetterValue = chr((letterValue - shift)%26 +65)
            oldMsg+=newLetterValue
    return oldMsg
        
        
   
x = encrypt("b","congratulations you cracked the cipher")
print(x)
