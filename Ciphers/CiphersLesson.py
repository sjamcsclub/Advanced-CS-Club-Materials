from string import ascii_uppercase as alpha
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


def solve(encryptedText):
    words = encryptedText.split(" ")  # splits string into words
    possible_combos = []
    for j in range(len(words)):
        temp = []
        ind = 1
        file.seek(0)  # Resets readline cursor to the beginning of the file

        while ind != 354980:  # length of file
            line = file.readline()  # reads a line from the wordlist
            line = cleanAll(line)  # cleans it to be a pretty string making it easy to encrypt and manipulate

            if len(line) == len(words[j]):
                # Checks that the line length matches the length of the encrypted string
                # as there is no point to check words that are longer or shorter than the encrypted one

                for i in range(len(alpha)):  # alpha is a string of  "abc...xyz"
                    # using the alphabet we are going to try all the simple shift possibilities
                    if encrypt(alpha[i], line) == words[j]:
                        # if the line encrypted with shift alpha[i] is equal to the encrypted word then we have found
                        # a possibility thus we will append it to temp
                        print("Answer is:", line)
                        temp.append(line)
            ind += 1

        possible_combos.append(temp)
        print(possible_combos)

what = getpass.getpass('Password:')
x = encrypt("x", what)
print(x)
solve(x)
