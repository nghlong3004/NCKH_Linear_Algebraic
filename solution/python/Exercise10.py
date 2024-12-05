# Define the price tables for shops S1 and S2
prices_S1 = {
    'Roll': 1.5, 
    'Bun': 2, 
    'Cake': 5, 
    'Bread': 16
}

prices_S2 = {
    'Roll': 1, 
    'Bun': 2.5, 
    'Cake': 4.5, 
    'Bread': 17
}

# Define the demanded quantities for each person
demanded_quantities = {
    'P1': {'Roll': 6, 'Bun': 5, 'Cake': 3, 'Bread': 2},
    'P2': {'Roll': 3, 'Bun': 6, 'Cake': 2, 'Bread': 2},
    'P3': {'Roll': 3, 'Bun': 4, 'Cake': 3, 'Bread': 1}
}

# Function to calculate the total cost for a person in a specific shop
def calculate_cost(person, shop_prices):
    total_cost = 0
    for item in shop_prices:
        total_cost += demanded_quantities[person][item] * shop_prices[item]
    return total_cost

# Determine the best shop for each person
best_shops = {}
for person in demanded_quantities:
    # Calculate the total cost for both shops
    cost_S1 = calculate_cost(person, prices_S1)
    cost_S2 = calculate_cost(person, prices_S2)
    
    # Choose the shop with the lower cost
    if cost_S1 < cost_S2:
        best_shops[person] = 'S1'
    else:
        best_shops[person] = 'S2'

# Output the result for each person
print("Optimal shop for each person:")
for person, shop in best_shops.items():
    print(f"{person} should shop at {shop}.")
