def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    d = {}
    for i in range (65, 91):
        if i + shift > 90:
            newShift = shift - (91 - i)
            d[chr(i)] = chr(65 + newShift)
        else:
            d[chr(i)] = chr(i + shift)
    for i in range (97, 123):
        if i + shift > 122:
            newShift = shift - (123 - i)
            d[chr(i)] = chr(97 + newShift)
        else:
            d[chr(i)] = chr(i + shift)
    return d

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    newStr = ''
    for cur in range (0, len(text)):
        if ord(text[cur]) >= 65 and ord(text[cur]) <=90 or ord(text[cur]) >= 97 and ord(text[cur]) <=122:
            newStr += coder[text[cur]]
        else:
            newStr += text[cur]
    return newStr

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    coder = buildCoder(shift)
    return applyCoder(text, coder)
text = "Congratulations you cracked the cipher!"
text = "Dpohsbuvmbujpot zpv dsbdlfe uif djqifs!"
a = applyShift(text, -1)
print(a)
