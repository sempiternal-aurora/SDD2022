def three_five(num):
    return (num%5==0 and num%3==0)

def three(num):
    return num%3==0
    
def five(num):
    return num%5==0

def FizzBuzz_Main():
    start = int(input("Enter the start: "))
    stop = int(input("Enter the end: "))
    for current_number in range(start, stop):
        if three_five(current_number):
            print("FizzBuzz")
        elif three(current_number):
            print("Fizz")
        elif five(current_number):
            print("Buzz")
        else:
            print(current_number)

if __name__ == "__main__":
    FizzBuzz_Main()

