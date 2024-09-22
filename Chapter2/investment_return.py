
principal = int(input("How much would you like to invest? : "))
rate = float(input("What is your investment rate? : "))
years = int(input("How many years you would like to invest? : "))

def calculate_money_invested(principal, rate, years):
    total_returns = principal (1 + rate) ** years
    return total_returns