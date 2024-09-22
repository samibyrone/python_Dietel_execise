
def is_number_multiple_of_4(number):
    results = []
    if number % 4 == 0: results.append(f"{number} is a multiple of 4")
    else: results.append(f"{number} is not a multiple of 4")
    return results

def is_number_multiple_of_10(number2):
    result = []
    if number2 % 10 == 0: result.append(f"{number2} is a multiple of 10")
    else: result.append(f"{number2} is not a multiple of 10")
    return result