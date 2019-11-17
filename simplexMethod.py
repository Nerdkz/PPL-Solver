import pulp
problem = pulp.LpProblem("Farmer", pulp.LpMaximize)

m1 = pulp.LpVariable('m1', lowBound=0, cat='Continuous')
m2 = pulp.LpVariable('m2', lowBound=0, cat='Continuous')
m3 = pulp.LpVariable('m3', lowBound=0, cat='Continuous')
m4 = pulp.LpVariable('m4', lowBound=0, cat='Continuous')

problem += 7 * m1 + 7 * m2 + 6 * m3 + 9 * m4, "Z"
problem += 4 * m1 + 5 * m2 + 3 * m3 + 5 * m4 <= 30000
problem += 2 * m1 + 1.5 * m2 + 3 * m3 + 3 * m4 <= 20000

problem.solve()

print("Problem status: " + pulp.LpStatus[problem.status])
print("Optimal M1: "+str(m1.value()))
print("Optimal M2: "+str(m2.value()))
print("Optimal M3: "+str(m3.value()))
print("Optimal M4: "+str(m4.value()))

print("By growing them the profit will be: "+str(pulp.value(problem.objective)))
