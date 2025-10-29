"""
Battery Modeling Tutorial - Loops and Conditionals
This file demonstrates Python loops and conditional statements through 
a practical battery charging/discharging simulation over 10 time periods.

Learning objectives:
- Using for loops 
- Working with conditional statements (if/elif/else)
- List indexing and manipulation
- Variable assignment and updates

Complete the script by filling in the missing code sections marked with <---.

1) Initially, ignore any battery constraints e.g. max/min state of charge, max power, efficiency, degradation etc
2) Revisit your completed code from (1) and add battery constraints. 
    You could do this by adding more nested if statements, or using min/max functions when calculating battery power.
3) finally, consider how you would model battery efficiency and degradation over time.

This is a comment block or docstring which can span multiple lines. 
It is often used at the start of files to describe the file.
@author: PLACE YOUR NAME HERE
"""

# Import any necessary libraries 
import math
import matplotlib.pyplot as plt

# Initialize battery parameters and variables
dt = 1  # Time step in hours
max_soc = 10  # Maximum state of charge (kWh)
min_soc = 1   # Minimum state of charge (kWh)
max_power = 15.0 # Maximum power the battery can handle (kW)
efficiency = 0.98    # Base battery efficiency
self_discharge = 0.01    # Battery self-discharge rate per time step
soc_0 = 5  # Initial state of charge (kWh)

# Create the demand variable as a list (this represents energy demand over 10 periods)
# Positive values indicate demand is needed from the battery
# Negative values indicate excess energy that can be used to charge the battery
demand_P = [5, -8, 12, -3, 7, -10, 15, -5, 8, -2]

# Initialize lists to store battery power, state of charge and the new net demand after battery operation
bat_P = [0] * len(demand_P)  # List to store battery power for each period, initialized to 0
soc_E = [0] * len(demand_P) # <--- List to store state of charge, starting at 5 kWh
net_demand_P = [0] * len(demand_P) # <--- List to store net demand after battery operation
deg = [0] * len(demand_P)

for i in range(len(demand_P)):
    # Conditional logic - check if demand is positive, negative or 0
    if demand_P[i] > 0:

        # Case (a): Positive demand means discharge the battery
        # Calculate battery power (discharge = negative internal battery power)
        discharge_P = min(demand_P[i], max_power)
        avai_SOC = soc_E[i-1]*(1-self_discharge) if i > 0 else soc_0 # Check if enough energy is available
        possible_discharge = min(discharge_P * dt, (avai_SOC - min_soc))/efficiency
        
        bat_P[i] = -possible_discharge / dt  # discharge (negative power)
        
    elif demand_P[i] < 0:
        # Case (b): Negative demand means charge the battery  
        # Calculate battery power (charging = positive internal power)
        charge_P = min(abs(demand_P[i]), max_power)
        avai_SOC = soc_E[i-1]*(1-self_discharge) if i > 0 else soc_0 # Check if enough energy is available
        possible_charge = min(charge_P * dt, (max_soc - avai_SOC))*efficiency
        
        bat_P[i] = possible_charge / dt  # charge (positive power)

    else:
        # Case (c): Zero demand means no battery operation
        bat_P[t] = 0  # No power change

# Update state of charge (SoC) based on battery power and time step
    if i == 0:
        soc_E[i] = soc_0*(1-self_discharge) + bat_P[i] * dt
    else:
        soc_E[i] = soc_E[i-1]*(1-self_discharge) + bat_P[i] * dt

    # Keep SoC within limits
    soc_E[i] = round(max(min_soc, min(max_soc, soc_E[i])),2)

    # update the net demand after battery operation
    net_demand_P[i] = round(demand_P[i] + bat_P[i],2)

# Print the final state of charge
print("Final State of Charge (kWh):", round(soc_E[-1],2))
print("State of Charge history:", soc_E)
print("Net Demand after battery operation:", net_demand_P) 

# Example data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Plot line graph
plt.plot(x, soc_E, color = 'blue')
plt.plot(x, net_demand_P, color = 'orange')

plt.legend()
plt.show()