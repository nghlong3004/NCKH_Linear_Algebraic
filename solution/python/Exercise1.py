import pulp

problem = pulp.LpProblem("Maximize_Income", pulp. LpMaximize)

x = pulp. LpVariable("x", lowBound=0, cat="Continuous")

y = pulp. LpVariable("y", lowBound=0, cat="Continuous") # Số giờ làm tại Công việc II


problem += 40 * x + 30 * y, "Total Income"

problem += x + y <= 12, "Total Working Hours"

problem += 2*x + y <= 16, "Preparation Time"

problem.solve()


print(f"Số giờ làm tại Công việc I: {x.varValue} giờ")

print(f"Số giờ làm tại Công việc II: {y.varValue} giờ")

print(f"Thu nhập tối đa: {pulp.value(problem.objective)} USD")
