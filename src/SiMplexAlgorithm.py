import numpy as np
from scipy.optimize import linprog

class LinearProgramming:
    def __init__(self, c, A, b, constraint_sense, objective='max'):
        self.c = np.array(c)
        self.A = np.array(A)
        self.b = np.array(b)
        self.constraint_sense = constraint_sense
        self.objective = objective.lower()

    def solve(self):
        if self.objective == 'max':
            obj = -self.c
        else:
            obj = self.c

        lhs_eq = []
        rhs_eq = []
        lhs_ub = []
        rhs_ub = []

        for idx, sense in enumerate(self.constraint_sense):
            if sense == '<=':
                lhs_ub.append(self.A[idx])
                rhs_ub.append(self.b[idx])
            elif sense == '>=':
                lhs_ub.append(-self.A[idx])
                rhs_ub.append(-self.b[idx])
            elif sense == '=':
                lhs_eq.append(self.A[idx])
                rhs_eq.append(self.b[idx])

        result = linprog(
            c=obj,
            A_ub=np.array(lhs_ub) if lhs_ub else None,
            b_ub=np.array(rhs_ub) if rhs_ub else None,
            A_eq=np.array(lhs_eq) if lhs_eq else None,
            b_eq=np.array(rhs_eq) if rhs_eq else None,
            method='highs'
        )

        return self._parse_result(result)

    def _parse_result(self, result):
        if result.success:
            optimal_value = -result.fun if self.objective == 'max' else result.fun
            solution = result.x
            status = 'Optimal solution found'
        elif result.status == 3:
            optimal_value = None
            solution = None
            status = 'Problem is infeasible'
        elif result.status == 2:
            optimal_value = None
            solution = None
            status = 'Problem is unbounded'
        else:
            optimal_value = None
            solution = None
            status = f'Solver encountered an issue: {result.message}'

        return {
            'status': status,
            'optimal_value': optimal_value,
            'solution': solution
        }


def user_input():
    objective = input("Enter objective type ('max' or 'min'): ").strip().lower()

    num_vars = int(input("Enter number of variables: "))
    c = []
    for i in range(num_vars):
        coeff = float(input(f"Enter coefficient for variable x{i+1}: "))
        c.append(coeff)

    num_constraints = int(input("Enter number of constraints: "))
    A = []
    b = []
    constraint_sense = []

    for i in range(num_constraints):
        print(f"\nConstraint {i+1}:")
        coeffs = []
        for j in range(num_vars):
            coeff = float(input(f"  Enter coefficient for x{j+1}: "))
            coeffs.append(coeff)
        sense = input("  Enter constraint sense ('<=', '>=', '='): ").strip()
        rhs = float(input("  Enter RHS value: "))

        A.append(coeffs)
        constraint_sense.append(sense)
        b.append(rhs)

    return c, A, b, constraint_sense, objective


if __name__ == '__main__':
    c, A, b, constraint_sense, objective = user_input()
    linearProgramming = LinearProgramming(c, A, b, constraint_sense, objective)
    result = linearProgramming.solve()

    print('\nStatus:', result['status'])
    if result['solution'] is not None:
        print('Optimal solution:', result['solution'])
        print('Optimal objective value:', result['optimal_value'])
