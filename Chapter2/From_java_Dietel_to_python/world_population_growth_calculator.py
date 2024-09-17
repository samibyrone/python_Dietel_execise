current_population_range = float(input("\nEnter Current World Population: "))
growth_rate = float(input("\nEnter The World Annual Population Growth Rate in %: ")) / 100
years = int(input("\nEnter The Number Years You want to Estimate: "))


def estimated_population_growth(current_population_range, growth_rate, years):
    return current_population_range * (1 + growth_rate) ** years


for count in range(1, years):
    population_estimate = estimated_population_growth(current_population_range, growth_rate, years)

print(f"\nThe Estimated World Population in {years} years: {population_estimate / 1_000_000_000:.9f} billion")
