import pulp
problem = pulp.LpProblem("Tank", pulp.LpMinimize)
x_1 = pulp.LpVariable('x_1', lowBound=0, cat='Integer')
x_2 = pulp.LpVariable('x_2', lowBound=0, cat='Integer')
x_3 = pulp.LpVariable('x_3', lowBound=0, cat='Integer')
x_4 = pulp.LpVariable('x_4', lowBound=0, cat='Integer')
x_5 = pulp.LpVariable('x_5', lowBound=0, cat='Integer')
x_6 = pulp.LpVariable('x_6', lowBound=0, cat='Integer')
problem += (5 * x_1) + (2.5 * x_2) + (0 * x_3) + (0 * x_4) + (12.5 * x_5) + (10 * x_6), "Z"
problem += (3 * x_1) + (2 * x_2) + x_3 >= 32
problem += (3 * x_1) + (2 * x_2) + x_3 <= 42
problem += x_2 + (2 * x_3) + x_5 >= 17
problem += x_2 + (2 * x_3) + x_5 <= 27
problem += x_4 + x_5 + (2 * x_6) >= 21
problem += x_4 + x_5 + (2 * x_6) <= 21
problem.solve()

print("problem status: " + pulp.LpStatus[problem.status])
print("Optimal amount to cut into x_1 = [15,15,15]: "+str(x_1.value()))
print("Optimal amount to cut into x_2 = [15,15,17.5]: "+str(x_2.value()))
print("Optimal amount to cut into x_3 = [15,17.5,17.5]: "+str(x_3.value()))
print("Optimal amount to cut into x_4 = [15,15,20]: "+str(x_4.value()))
print("Optimal amount to cut into x_5 = [17.5,20]: "+str(x_5.value()))
print("Optimal amount to cut into x_6 = [20,20]: "+str(x_6.value()))
print("The total metal loss is: "+str(pulp.value(problem.objective)))

plate15 = (3 * x_1.value()) + (2 * x_2.value()) + x_3.value()
plate17 = x_2.value() + (2 * x_3.value()) + x_5.value()
plate20 = x_4.value() + x_5.value() + (2 * x_6.value())

print("Total of 15cm plates "+str(plate15))
print("Total of 17.5cm plates "+str(plate17))
print("Total of 20cm plates "+str(plate20))
