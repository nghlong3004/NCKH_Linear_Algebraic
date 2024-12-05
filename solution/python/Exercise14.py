import numpy as np

# Define the coefficients of the system of equations
A = np.array([
    [1, -0.65, -0.55],  # x1 = 50000 + 0.65x2 + 0.55x3
    [-0.25, 0.95, -0.1],  # x2 = 25000 + 0.25x1 + 0.05x3
    [-0.25, -0.05, 1]    # x3 = 0.25x1 + 0.1x2
])

# Define the constants on the right-hand side of the equations
b = np.array([50000, 25000, 0])

# Solve the system of linear equations
output_values = np.linalg.solve(A, b)

# Extract the results
x1, x2, x3 = output_values

# Output the results
print(f"Total output value of Coal Mine (x1): {x1:.2f} yuan")
print(f"Total output value of Power Plant (x2): {x2:.2f} yuan")
print(f"Total output value of Local Railway (x3): {x3:.2f} yuan")

# Calculate payments between companies
payment_coal_to_power = 0.25 * x2
payment_coal_to_railway = 0.25 * x1
payment_power_to_railway = 0.05 * x2
payment_power_to_coal = 0.65 * x2
payment_railway_to_coal = 0.55 * x3
payment_railway_to_power = 0.05 * x2

# Output the payment details
print(f"Coal Mine pays {payment_coal_to_power:.2f} yuan to Power Plant")
print(f"Coal Mine pays {payment_coal_to_railway:.2f} yuan to Local Railway")
print(f"Power Plant pays {payment_power_to_railway:.2f} yuan to Local Railway")
print(f"Power Plant pays {payment_power_to_coal:.2f} yuan to Coal Mine")
print(f"Local Railway pays {payment_railway_to_coal:.2f} yuan to Coal Mine")
print(f"Local Railway pays {payment_railway_to_power:.2f} yuan to Power Plant")

# Calculate the value created by each company
value_created_coal = x1 - (payment_coal_to_power + payment_coal_to_railway)
value_created_power = x2 - (payment_power_to_railway + payment_power_to_coal)
value_created_railway = x3 - (payment_railway_to_coal + payment_railway_to_power)

# Output the value created by each company
print(f"Value created by Coal Mine: {value_created_coal:.2f} yuan")
print(f"Value created by Power Plant: {value_created_power:.2f} yuan")
print(f"Value created by Local Railway: {value_created_railway:.2f} yuan")
