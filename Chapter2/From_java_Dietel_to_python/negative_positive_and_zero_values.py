print("Enter Ten Numbers to Check: ")

positive = 0
negative = 0
zero = 0

for index in range(10):
    numbers = float(input())
    if numbers > 0: positive += 1
    elif numbers < 0: negative += 1
    else: zero += 1

print("\nWe Have %d%n Positive numbers: ", positive)
print("\nWe Have %d%n Negative numbers: ", negative)
print("\nWe Have %d%n Zero numbers: ", zero)