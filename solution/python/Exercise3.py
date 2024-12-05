import pulp

# Khởi tạo bài toán tối ưu

problem = pulp. LpProblem("Maximize_Profit_NutCompany", pulp. LpMaximize)

# Khai báo các biến

a = pulp. LpVariable("a", lowBound=0, cat="Continuous")

# Số Lượng pound Hỗn hợp A

b = pulp. LpVariable("b", lowBound=0, cat="Continuous") # Số lượng pound Hỗn hợp B

# Hàm mục tiêu (maximize lợi nhuận)

problem += 4 * a + 5 * b, "Total Profit"

# Các ràng buộc

problem += a + b <= 1440, "Peanuts"

problem += 3 *a + 2 * b <= 3840, "Almonds"

problem += a + 2 * b <= 2560, "Cashews"

# Giải bài toán

problem.solve()

# In kết quả

print(f"Số lượng pounds Hỗn hợp A: {a.varValue} lb")

print(f"Số lượng pounds Hỗn hợp B: {b.varValue} lb")

print (f"Lợi nhuận tối đa: {pulp.value(problem.objective)} USD")
