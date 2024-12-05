# Initial conditions
M0 = 8000  # Married women at year 0
S0 = 2000  # Single women at year 0

# Transition probabilities
married_to_married = 0.7
single_to_married = 0.2
married_to_single = 0.3
single_to_single = 0.8

# Number of years to calculate
years = 2

# Variables to store results
results = [(M0, S0)]

# Iterative calculation for each year
for t in range(years):
    # Current married and single women
    M_t, S_t = results[-1]
    
    # Calculate the next year values
    M_next = married_to_married * M_t + single_to_married * S_t
    S_next = married_to_single * M_t + single_to_single * S_t
    
    # Store the results
    results.append((M_next, S_next))

# Print results
for year, (married, single) in enumerate(results):
    print(f"Year {year}: Married = {married}, Single = {single}")
