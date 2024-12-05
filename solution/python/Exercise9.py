import numpy as np

# Initial population percentages
C_t = 30  # City population percentage at t=0
S_t = 70  # Suburb population percentage at t=0

# Transition matrix A
A = np.array([[0.94, 0.02],
              [0.06, 0.98]])

# Initial population vector
population = np.array([C_t, S_t])

# Function to compute population after n years
def population_after_years(population, matrix, years):
    for _ in range(years):
        population = np.dot(matrix, population)
    return population

# Compute populations after 10, 30, and 50 years
pop_10_years = population_after_years(population, A, 10)
pop_30_years = population_after_years(population, A, 30)
pop_50_years = population_after_years(population, A, 50)

print(f"Population after 10 years: {pop_10_years}")
print(f"Population after 30 years: {pop_30_years}")
print(f"Population after 50 years: {pop_50_years}")
