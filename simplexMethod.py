import pulp
problem = pulp.LpProblem("Farmer", pulp.LpMaximize)

a = pulp.LpVariable('a', lowBound=0, cat='Continuous')
b = pulp.LpVariable('b', lowBound=0, cat='Continuous')
c = pulp.LpVariable('c', lowBound=0, cat='Continuous')


problem += 5 * a + 7 * b + 8 * c, "Z"
problem += 1 * a + 1 * b + 2 * c <= 1190
problem += 3 * a + 4.5 * b + 1 * c <= 4000

problem.solve()

print("Problem status: " + pulp.LpStatus[problem.status])
print("Optimal A: "+str(a.value()))
print("Optimal B: "+str(b.value()))
print("Optimal C: "+str(c.value()))

print("By growing them the profit will be: "+str(pulp.value(problem.objective)))
