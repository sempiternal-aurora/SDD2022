def userInput():
    length = int(input("Length: "))
    height = int(input("Height: "))
    return length, height

def calcArea(l, h):
    A = l * h
    return A

def display(area):
    print("\nArea:", area)

def main():
    length, height = userInput()
    area = calcArea(length, height)
    display(area)

if __name__ == "__main__":
    main()