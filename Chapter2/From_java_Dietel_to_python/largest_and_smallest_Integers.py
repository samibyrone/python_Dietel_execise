first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))
fourth = int(input("Enter the fourth number: "))
fiveth = int(input("Enter the fiveth number: "))

smallest = first
if second < smallest: smallest = second
if third < smallest: smallest = third
if fourth < smallest: smallest = fourth
if fiveth < smallest: smallest = fiveth

largest = first
if second > largest: largest = second
if third > largest: largest = third
if fourth > largest: largest = fourth
if fiveth > largest: largest = fiveth

print('\nThe smallest integer in the group of five integer is: ', smallest)
print('\nThe largest integer in the group of five integer is: ', largest)
