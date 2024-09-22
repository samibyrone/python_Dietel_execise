
def sorting_three_numbers():
    number1 = int(input("\nEnter the first number: "))
    number2 = int(input("\nEnter the second number: "))
    number3 = int(input("\nEnter the third number: "))

    print(f"\nNumber inputs: {number1}, {number2}, {number3}")

    if number1 > number2: number1, number2 = number2, number1
    if number1 > number3: number1, number3 = number3, number1
    if number2 > number3: number2, number3 = number3, number2


    print("Numbers in increasing order:", number1, number2, number3)

sorting_three_numbers()
