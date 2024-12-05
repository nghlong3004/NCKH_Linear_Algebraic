from pulp import LpProblem, LpVariable, LpMinimize

# Create the optimization problem
prob = LpProblem("Minimize_Chemicals", LpMinimize)

# Define the variables (moles of N2, H2, O2)
x = LpVariable("x", lowBound=0, cat='Continuous')  # moles of N2
y = LpVariable("y", lowBound=0, cat='Continuous')  # moles of H2
z = LpVariable("z", lowBound=0, cat='Continuous')  # moles of O2

# Define the objective function (we don't actually minimize anything in this case, just to fulfill the form)
prob += x + y + z, "Total Chemicals Used"

# Constraints based on the chemical reactions:
# First constraint: 8 moles of HNO3 require 8 moles of NO2, and 2 moles of NO2 come from 1 mole of N2
prob += x == 8, "Nitrogen Moles for HNO3"  # From reaction 1 (1 mole N2 for 2 moles NH3)

# Second constraint: 3 moles of O2 are required for 4 moles of NH3, and NH3 comes from N2
prob += z == (3 * x) / 4, "Oxygen Moles for NO2"

# Third constraint: 3 moles of H2 are required for every 1 mole of N2 to produce NH3
prob += y == 3 * x, "Hydrogen Moles for NH3"

# Solve the problem
prob.solve()

# Print the results
print(f"Moles of Nitrogen (N2): {x.varValue}")
print(f"Moles of Hydrogen (H2): {y.varValue}")
print(f"Moles of Oxygen (O2): {z.varValue}")
