nums = 5
for index in range (nums):
    print("*", end=" ")
    for index2 in range (nums):
        print("*", end=" ")
        if (index == 0 or index2 == nums - 1):
            print("*", end = " ")
        else: print("", end = " ")
        print( )