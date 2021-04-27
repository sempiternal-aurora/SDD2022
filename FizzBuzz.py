def three_five(num):
    if num%5==0 and num%3==0: return True
    else: return False

def three(num):
    if num%3==0: return True
    else: return False
    
def five(num):
    if num%5==0: return True
    else: return False

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

