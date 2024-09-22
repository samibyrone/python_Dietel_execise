
first = int(input("Enter your first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

add = first + second + third

average = add / 3

product = first * second * third

smallest = first
if second < smallest: smallest = second
if third < smallest: smallest = third

largest = first
if second > largest: largest = second
if third > largest: largest = third

print('\nThe sum of all numbers is ', add)
print('\nThe average of all numbers is ', average)
print('\nThe product of all numbers is ', product)
print('\nThe smallest number is ', smallest)
print('\nThe largest number is ', largest)