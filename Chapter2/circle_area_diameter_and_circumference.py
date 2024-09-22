radius = 2
pi = 3.14159

def circle_of_area(radius, pi):
    area = pi * radius * radius
    return area

circle_area = circle_of_area == pi * (radius ** 2)
print('The area of the circle is: ', circle_area)


def circle_of_diameter(radius):
    diameter = 2 * radius
    return diameter

circle_diameter = circle_of_diameter == 2 * radius
print('The diameter of the circle is: ', circle_diameter)


def circle_of_circumference(radius, pi):
    circumference = 2 * pi * radius
    return circumference

circle_circumference = circle_of_circumference == 2 * pi * radius
print("The circumference of the circle is: ", circle_circumference)
