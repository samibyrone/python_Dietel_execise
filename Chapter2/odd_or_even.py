number = int(input("Enter a number: "))

def is_number_even(number):
    if number % 2 == 0: return True
    else: return False

if is_number_even(number): print(f"{number} is even.")
else: print(f"{number} is odd.")
