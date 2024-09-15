number = int(input('Enter a number: '))

sqrt = number * number

print('\nThe number is ', number, 'and the square root is ', sqrt)
if (sqrt >= 100): print(f'\nThis number ',number, " and it's square ",sqrt, "is less than 100")
elif (sqrt <= 100): print(f'\nThis number ',number, " and it's square ",sqrt, "is greater than 100")
elif (sqrt != 100): print(f'\nThis number ',number, " and it's square ",sqrt, "is equal to 100")
elif (sqrt == 100): print(f'\nThis number ',number, " and it's square ",sqrt, "is not equal to 100")