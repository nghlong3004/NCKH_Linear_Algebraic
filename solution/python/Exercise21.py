import numpy as np

# Initial state: 200 interested in Mathematics, 350 interested in Biology
M_initial = 200
B_initial = 350

# Transition matrix
transition_matrix = np.array([[0.92, 0.04],  # 0.92 for M staying M, 0.04 for B to M
                              [0.08, 0.96]]) # 0.08 for M to B, 0.96 for B staying B

# Function to compute the number of people after n years
def calculate_population_after_years(M_initial, B_initial, years):
    state = np.array([M_initial, B_initial])  # initial state vector [M(0), B(0)]
    
    # Apply the transition matrix for the given number of years
    for _ in range(years):
        state = np.dot(transition_matrix, state)
    
    # Apply custom rounding
    M_after_years = round(state[0])  # Number of people interested in Mathematics
    B_after_years = round(state[1])  # Number of people interested in Biology
    
    return M_after_years, B_after_years

# Part a) After 15 years, how many are interested in Mathematics?
M_15_years, _ = calculate_population_after_years(M_initial, B_initial, 15)
print(f"Number of people interested in Mathematics after 15 years (rounded): {M_15_years}")

# Part b) After 20 years, how many are interested in Biology?
_, B_20_years = calculate_population_after_years(M_initial, B_initial, 20)
print(f"Number of people interested in Biology after 20 years (rounded): {B_20_years}")
