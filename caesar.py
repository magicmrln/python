def caesar(str, offset):
    strOut = ""
    for i in range(len(str)):
        strOut += caesarChar(str[i], offset)
    return strOut

def caesarChar(char, offset):
    index = ord(char)
    if index == 32: # leertasten check
        return " "
    base = 65 # 65(gross) oder 97(klein) ; base = start in der ascii tabelle
    if char.islower():
        base = 97
    newIndex = (index - base + offset) % 26 + base
    char = chr(newIndex)
    return char

print("---------- caesar cipher ----------")
inStr = input("string: ")
inOffset = int(input("offset: "))
print("")
out = caesar(inStr, inOffset)
print(out)
print("")
