import re
import getpass

file = open("words.txt", "r")


def sanitize(msg, key):
    return msg.upper(), key.upper()


def encrypt(encKey, message):
    newMsg = ""
    msg, key = sanitize(message, encKey)
    for i in range(len(msg)):
        if ord(msg[i]) == ord(" "):

            newMsg += " "
        else:
            letterValue = ord(msg[i])
            shift = ord(key[i % len(key)])
            newLetterValue = chr((letterValue + shift) % 26 + 65)
            newMsg += newLetterValue
    return newMsg


def decrypt(decKey, message):
    oldMsg = ""
    msg, key = sanitize(message, decKey)
    for i in range(len(msg)):
        if ord(msg[i]) == ord(" "):
            oldMsg += " "

        else:
            letterValue = ord(msg[i])
            shift = ord(key[i % len(key)])
            newLetterValue = chr((letterValue - shift) % 26 + 65)
            oldMsg += newLetterValue
    return oldMsg


def cleanAll(string):
    rx = re.compile('\W+')
    return rx.sub(" ", string).strip()


def intToChar(integer):
    return chr(integer+65)


def solve(encryptedText):
    words = encryptedText.split(" ")  # splits string into words
    possible_combos = []
    for j in range(len(words)):
        temp = []
        file.seek(0)  # Resets readline cursor to the beginning of the file

        for line in file:
            # read a line from the wordlist
            line = cleanAll(line)  # cleans it to be a pretty string making it easy to encrypt and manipulate

            # Checks that the line length matches the length of the encrypted string
            # as there is no point to check words that are longer or shorter than the encrypted one
            if len(line) == len(words[j]):

                for i in range(26):
                    # using the alphabet we are going to try all the simple shift possibilities
                    if encrypt(intToChar(i), line) == words[j]:
                        # if the line encrypted with shift  is equal to the encrypted word then we have found
                        # a possibility thus we will append it to temp
                        key = (intToChar(i))
                        print("Answer is:", line, key)
                        temp.append(line)
        possible_combos.append(temp)
        print(possible_combos)


# what = getpass.getpass('Password:')
what = input("Enter Some Text")
print("Encrypted Message:",what)
x = encrypt("x", what)
print(x)
solve(x)
##sleep(100)
