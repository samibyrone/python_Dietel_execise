print(f"{'Number': <10} {'Square': <10} {'Cube': <10}")

for number in range(11):
    square = number ** 2
    cube = number ** 3

    print(f"{number: <10} {square: <10} {cube: <10}")