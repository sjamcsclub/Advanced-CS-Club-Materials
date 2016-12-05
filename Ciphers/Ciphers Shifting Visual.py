from string import ascii_uppercase as alpha

def showShift(key):
    dispStr = ""
    for i in range(len(alpha)):
        letterValue = ord(alpha[i])
        shift = ord(key[i%len(key)])
        newLetterValue = chr((letterValue + shift)%26 +65)
        dispStr+=newLetterValue
    return dispStr

print(alpha)
print(showShift("XC"))

    
