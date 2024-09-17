number = int(input('Enter your five digit number: '))

index1 = number // 10000
index2 = (number // 1000) % 10
index3 = (number // 100) % 10
index4 = (number // 10) % 10
index5 = number % 10

print(index1, index2, index3, index4, index5)