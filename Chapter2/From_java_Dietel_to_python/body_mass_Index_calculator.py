weight = float(input("Enter Your Weight in (kg): "))
height = float(input("Enter Your Height in (m): "))


def body_mass_calculator(weight, height):
    bodyMassIndex = weight / (height * height)
    return bodyMassIndex

calculate = body_mass_calculator(weight, height)
print(f"\nYOUR BODY MASS INDEX IS: , {calculate:.2f}.")


if calculate < 17.5: print('Your are UnderWeight')
elif calculate < 25.5: print('You Have a Normal Weight')
elif calculate < 31.5: print('You are Getting Overweight')
else: print('You Have Too Much Obesity, You Really need to Work on Yourself')


