import pulp

problem = pulp. LpProblem("Maximize_Profit_Factory", pulp. LpMaximize)

# Khai báo các biến

r = pulp. LpVariable("r", lowBound=0, cat="Continuous") # Số Lượng thiết bị loại thường

p = pulp. LpVariable("p", lowBound=0, cat="Continuous") # Số Lượng thiết bị loại cao cấp

# Hàm mục tiêu (maximize lợi nhuận) problem += 20 * r + 30* p, "Total Profit"

# Các ràng buộc

problem += 20 * r + 30* p, "Total Profit"

problem += r + 2* p <= 12, "Assembly Time"

problem += 2 * r + p <= 12, "Finishing Time"

problem += r + p <= 7, "Production Limit"

# Giải bài toán

problem.solve()

# In kết quả

print(f"Số lượng thiết bị loại thường: {r.varValue} thiết bị")

print(f"Số lượng thiết bị loại cao cấp: {p.varValue} thiết bị")

print (f"Lợi nhuận tối đa: {pulp.value(problem.objective)} USD")
