index = 10
for num1 in range (index):
    for num2 in range (index):
        if (num1 + num2) % 2 == 0:
         print(" *", end=" ")
        else:
            print("* ", end=" *")
    print()