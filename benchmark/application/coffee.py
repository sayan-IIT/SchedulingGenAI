import time
from gurobipy import GRB, Model

# Example data

capacity_in_technician = {'Adam': 150, 'John': 50, 'Dave': 100}

Technician_Cost = {
    ('Adam', 'Internal'): 5,
    ('Adam', 'External'): 4,
    ('John', 'Internal'): 6,
    ('John', 'External'): 3,
    ('Dave', 'Internal'): 2,
    ('Dave', 'External'): 7
}

maintenance_time= {'Internal': 3, 'External': 5}

repair_time= {'Internal': 5, 'External': 6}

Travel_Cost = {
    ('Internal', 'Customer_Site_1'): 5,
    ('Internal', 'Customer_Site_2'): 3,
    ('Internal', 'Customer_Site_3'): 6,
    ('External', 'Customer_Site_1'): 4,
    ('External', 'Customer_Site_2'): 5,
    ('External', 'Customer_Site_3'): 2
}

maintenance_work = {'Customer_Site_1': 20, 'Customer_Site_2': 30, 'Customer_Site_3': 40}

repair_work = {'Customer_Site_1': 20, 'Customer_Site_2': 20, 'Customer_Site_3': 100}

customers = list(set(i[1] for i in Travel_Cost.keys()))
skills = list(
    set(i[1] for i in Technician_Cost.keys()))
technicians = list(
    set(i[0] for i in Technician_Cost.keys()))

# Create a new model
model = Model("GBS Field Scheduling")

# OPTIGUIDE DATA CODE GOES HERE

# Create variables
x = model.addVars(Technician_Cost.keys(),
                  vtype=GRB.INTEGER,
                  name="x")
y_light = model.addVars(Travel_Cost.keys(),
                        vtype=GRB.INTEGER,
                        name="y_light")
y_dark = model.addVars(Travel_Cost.keys(),
                       vtype=GRB.INTEGER,
                       name="y_dark")

# Set objective
model.setObjective(
    sum(x[i] * Technician_Cost[i]
        for i in Technician_Cost.keys()) +
    sum(maintenance_time[r] * y_light[r, c] +
        repair_time[r] * y_dark[r, c]
        for r, c in Travel_Cost.keys()) + sum(
            (y_light[j] + y_dark[j]) * Travel_Cost[j]
            for j in Travel_Cost.keys()), GRB.MINIMIZE)

# Conservation of flow constraint
for r in set(i[1] for i in Technician_Cost.keys()):
    model.addConstr(
        sum(x[i] for i in Technician_Cost.keys()
            if i[1] == r) == sum(
                y_light[j] + y_dark[j]
                for j in Travel_Cost.keys()
                if j[0] == r), f"flow_{r}")

# Add supply constraints
for s in set(i[0] for i in Technician_Cost.keys()):
    model.addConstr(
        sum(x[i] for i in Technician_Cost.keys()
            if i[0] == s) <= capacity_in_technician[s], f"supply_{s}")

# Add demand constraints
for c in set(i[1] for i in Travel_Cost.keys()):
    model.addConstr(
        sum(y_light[j] for j in Travel_Cost.keys()
            if j[1] == c) >= maintenance_work[c],
        f"maintenance_demand_{c}")
    model.addConstr(
        sum(y_dark[j] for j in Travel_Cost.keys()
            if j[1] == c) >= repair_work[c],
        f"repair_demand_{c}")

# Optimize model
model.optimize()
m = model

# OPTIGUIDE CONSTRAINT CODE GOES HERE

# Solve
m.update()
model.optimize()

print(time.ctime())
if m.status == GRB.OPTIMAL:
    print(f'Optimal cost: {m.objVal}')
else:
    print("Not solved to optimality. Optimization status:", m.status)
