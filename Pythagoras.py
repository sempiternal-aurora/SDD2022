def sideIncluded(a, b):
    c = (((a**2)-(b**2))**0.5)
    return c

def sideExcluded(a, b):
    c = (((a**2)+(b**2))**0.5)
    return c

def getSides():
    a = int(input("Side 1: "))
    b = int(input("Side 2: "))
    input1 = input("Is one of the two sides the hypotenuse? (y/n): ").lower()
    if input1 == 'y' or input1 == 'yes':
        hyinclu = True
    else:
        hyinclu = False
    if b > a:
        c = a
        a = b
        b = c
    return a, b, hyinclu

def main():
    a, b, included = getSides()
    if included == True:
        c = sideIncluded(a, b)
    else:
        c = sideExcluded(a, b)
    print("Unknown Side:", c)

if __name__ == "__main__":
    main()