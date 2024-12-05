from pulp import LpProblem, LpVariable, LpMinimize, LpConstraint, LpAffineExpression

# Khởi tạo bài toán tối ưu
prob = LpProblem("Minimize_Cost", LpMinimize)

# Định nghĩa các biến quyết định
x = LpVariable("x", lowBound=1, cat='Continuous')  # Số giờ làm việc của John, x >= 1
y = LpVariable("y", lowBound=1, cat='Continuous')  # Số giờ làm việc của Mary, y >= 1

# Hàm mục tiêu: C = 15x + 25y
prob += 15*x + 25*y, "Total Cost"

# Các ràng buộc
prob += 20*x + 30*y >= 110, "Minimum Number of Papers"

# Giải bài toán
prob.solve()

# In kết quả
print(f"John's working hours per week (x): {x.varValue}")
print(f"Mary's working hours per week (y): {y.varValue}")
print(f"Total cost (C): {prob.objective.value()}")
