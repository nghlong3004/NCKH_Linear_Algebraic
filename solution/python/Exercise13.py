# Initial funds for company A and B
x = 28  # Company A's initial funds
y = 26  # Company B's initial funds

# Calculate final funds for both companies after transfers
A_prime = 0.88 * x + 0.1 * y
B_prime = 0.9 * y + 0.12 * x

# Output the results
print(f"Final funds for Company A: {A_prime} million yuan")
print(f"Final funds for Company B: {B_prime} million yuan")

# Check if any mobilization of funds is required
minimum_fund = 24  # The minimum required funds for each company
if A_prime < minimum_fund or B_prime < minimum_fund:
    print("Mobilization of funds is required to meet the minimum requirement.")
else:
    print("No mobilization of funds is necessary.")
