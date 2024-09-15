index = int(input('Enter the first number: '))
index2 = int(input('Enter the second number: '))

triple = index * 3
doubled = index2 * 2
result = triple % doubled

if triple % doubled == 0: print("The number ",triple," is a multiple of ",doubled,"\n The result is ", result)
else: print("The number ",triple," is not a multiple of ",doubled)