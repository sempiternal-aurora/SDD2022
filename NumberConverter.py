
def bin2dec(binword):
    decnum = 0
    binword = binword[::-1]
    for i in range(len(binword)):
        if binword[i] == "1":
            decnum += 2**i
    return decnum

def dec2oct(decnum):
    octword = ""
    while decnum > 0:
        octword = str(decnum % 8) + octword
        decnum = decnum // 8
    return octword

def bin2oct(binnum):
    decnum = bin2dec(binnum)
    octword = dec2oct(decnum)
    return octword

def dec2hex(decnum):
    hexword = ""
    while decnum > 0:
        newindex = str(decnum % 16)
        newindex = dec2hexindex(int(newindex))
        hexword = newindex + hexword
        decnum = decnum // 16
    return hexword

def dec2hexindex(index):
    if index <= 9:
        return str(index)
    elif index == 10:
        return "A"
    elif index == 11:
        return "B"
    elif index == 12:
        return "C"
    elif index == 13:
        return "D"
    elif index == 14:
        return "E"
    elif index == 15:
        return "F"

def bin2hex(binnum):
    decnum = bin2dec(binnum)
    hexword = dec2hex(decnum)
    return hexword

def dec2bin(decnum):
    binword = ""
    while decnum > 0:
        binword = str(decnum % 2) + binword
        decnum = decnum // 2
    return binword

def userinput():
    strnumber = input("Enter a number: ")
    numformat = input("What form is the number (B,O,D,H): ")
    convertto = input("What do you want to convert the number to? (B,O,D,H): ")
    return numformat.lower(), convertto.lower(), strnumber

def main():
    numformat, convertto, strnumber = userinput()
    if numformat == "b":
        if convertto == "b":
            connumber = strnumber
        if convertto == "o":
            connumber = bin2oct(strnumber)
        elif convertto == "d":
            connumber = bin2dec(strnumber)
        elif convertto == "h":
            connumber = bin2hex(strnumber)
        else:
            connumber = "That format is not recognised"
    elif numformat == "o":
        print("no")
    elif numformat == "d":
        if convertto == "b":
            connumber = dec2bin(int(strnumber))
        elif convertto == "o":
            connumber = dec2oct(int(strnumber))
        elif convertto == "d":
            connumber = int(strnumber)
        elif convertto == "h":
            connumber = dec2hex(int(strnumber))
        else:
            connumber = "That format is not recognised"
    elif numformat == "h":
        print("no")
    else:
        connumber = "That format is not recognised"
    print(connumber)

if __name__ == "__main__":
    main()