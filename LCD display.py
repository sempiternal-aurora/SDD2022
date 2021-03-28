def user_input():
    #A very nice program that asks the user to input a number and a size
    number = input("Hello there, what number do you want to be LCD’d (0 ≤ n ≤ 99999999)? ")
    while len(number) > 8 or len(number) == 0 or number.isnumeric() == False:
        number = input("That is not a valid number, could you please try again (0 ≤ n ≤ 99999999)? ")
    size = int(input("And how large would you like that number to be (1 ≤ s ≤ 10)? "))
    while size < 1 or size > 10:
        size = input("That is not a valid size, could you please try again (1 ≤ s ≤ 10)? ")
    return size, number

def segment_char(digit, segment_id):
    #Based on the very complex segment design I made, this program returns the correct character for each segment of every number
    digit = digit
    if segment_id % 2 == 0: #This is all of the middle and corner segments, how nice that they're all even
        char = " "
    elif segment_id == 1: #top segment
        if digit == 1 or digit == 4:
            char = " "
        else:
            char = "-"
    elif segment_id == 3: #top left segment
        if digit == 1 or digit == 2 or digit == 3:
            char = " "
        else:
            char = "|"
    elif segment_id == 5: #top right segment
        if digit == 5 or digit == 6:
            char = " "
        else:
            char = "|"
    elif segment_id == 7: #middle segment
        if digit == 1 or digit == 7 or digit == 0:
            char = " "
        else:
            char = "-"
    elif segment_id == 9: #bottom left segment
        if digit == 2 or digit == 6 or digit == 8 or digit == 0:
            char = "|" #Did it the other way round for this one because this is the one segment where there is more numbers without it then with it
        else:
            char = " "
    elif segment_id == 11: #Bottom right segment
        if digit == 2:
            char = " "
        else:
            char = "|"
    elif segment_id == 13: #Bottom segment
        if digit == 1 or digit == 4 or digit == 7:
            char = " "
        else:
            char = "-"
    return char

def generate_digit_line(line_id, digit, size):
    #Takes each digit, and what line of the number it is taking, and generates that line, before returning it
    digit_line = ""
    for c in range(0, 3):
        segment_id = 3 * line_id + c
        char = segment_char(digit, segment_id)
        if c == 1:
            digit_line = digit_line + (char * size)
        else:
            digit_line = digit_line + char
    return digit_line

def generate_line(line_id, number, size):
    #makes each digit in a line in order, adding them all to one string, which is the finished line, and returns that finished line
    lcd_line = ""
    for digit in number:
        digit_line = generate_digit_line(line_id, int(digit), size)
        lcd_line = lcd_line + digit_line + " "
    lcd_line = lcd_line[:-1]
    return lcd_line

def generate_display(size, number):
    #
    line_id = 0
    while line_id < 5:
        lcd_line = generate_line(line_id, number, size)
        if line_id % 2 == 0:
            print(lcd_line)
        elif line_id % 2 == 1:
            for i in range(0, size):
                print(lcd_line)
        line_id += 1
    print("")

def main():
    size, number = user_input()
    generate_display(size, number)

if __name__ == "__main__":
    main()