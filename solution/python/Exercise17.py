import numpy as np

# Product data (prices and quantities sold per day for each product)
products = ['Product1', 'Product2', 'Product3', 'Product4']
prices = [0.5, 0.4, 0.3, 4.5]  # Replace with actual product prices

# Quantities sold per day (Mon-Sun) for each product (replace with your data)
quantities_per_day = [
    [20, 25, 15, 18, 22, 40, 36],  # Quantities sold per day for Product1 (Mon-Sun)
    [30, 18, 24, 23, 26, 55, 40],  # Quantities sold per day for Product2
    [15, 8, 6, 10, 5, 22, 30],  # Quantities sold per day for Product3
    [4, 3, 6, 5, 2, 10, 9]   # Quantities sold per day for Product4
]

# Calculate daily income for each product
daily_incomes = []

for i in range(len(products)):
    # Multiply quantities sold by price per unit for each day (Mon-Sun)
    daily_income = np.array(quantities_per_day[i]) * prices[i]
    daily_incomes.append(daily_income)

# Calculate total daily income (sum of incomes from all products)
total_daily_income = np.sum(daily_incomes, axis=0)

# Calculate total weekly income (sum of daily income over 7 days)
total_weekly_income = np.sum(total_daily_income)

# Display daily income and total weekly income
for i, product in enumerate(products):
    print(f"Daily income for {product}: {daily_incomes[i]}")

print(f"\nTotal daily income of the store: {total_daily_income}")
print(f"Total weekly income of the store: {total_weekly_income:.2f}")
