# Given data
products = ['Rice', 'Wine', 'Oil', 'Flour']
cost_prices = [30, 50, 20, 15]  # Example cost prices for rice, wine, oil, flour (in currency units)
profit_margins_percent = [10, 8, 5, 4]  # Expected profit margins (in percentage)

# Calculate the selling price based on profit margin
def calculate_selling_price(cost_price, profit_margin_percent):
    return cost_price * (1 + profit_margin_percent / 100)

# Calculate selling prices and verify profit margins
selling_prices = []
calculated_profit_margins = []

for i, product in enumerate(products):
    selling_price = calculate_selling_price(cost_prices[i], profit_margins_percent[i])
    selling_prices.append(selling_price)

    # Recalculate the profit margin for verification
    actual_margin = ((selling_price - cost_prices[i]) / cost_prices[i]) * 100
    calculated_profit_margins.append(actual_margin)

# Display the results
for i, product in enumerate(products):
    print(f"For {product}:")
    print(f"  Expected Profit Margin: {profit_margins_percent[i]}%")
    print(f"  Calculated Profit Margin: {calculated_profit_margins[i]:.2f}%\n")
