import math
import pandas as pd
import numpy as np
import os

# Define a function to size a PV system based on building dimensions and panel specifications
def calculate_pv_size(building_length, building_width, roof_angle, panel_width, panel_height, panel_power):
    # Convert roof angle from degrees to radians for math.cos()
    roof_angle_rad = math.radians(roof_angle)
    
    # Calculate effective roof area (convert building dimensions to mm)
    building_area = (building_length * 1e3 * building_width * 1e3) / math.cos(roof_angle_rad)
    
    # Number of panels that fit on the roof
    num_panels = building_area // (panel_width * panel_height)
    
    # Total PV capacity (Wp)
    total_pv_cap_wp = num_panels * panel_power
    
    # Convert to kW
    total_pv_cap_kw = total_pv_cap_wp / 1000
    
    return total_pv_cap_kw, num_panels

# Example inputs
panel_width = 1046  # mm
panel_height = 1690  # mm
panel_power = 400  # Wp
building_length = 31  # m
building_width = 7.5  # m
roof_angle = 22       # degrees

# Call the function
pv_capacity_kw, num_panels = calculate_pv_size(building_length, building_width, roof_angle, panel_width, panel_height, panel_power)

# Display results
print(f"Number of PV panels: {num_panels:.0f}")
print(f"Total PV capacity: {pv_capacity_kw:.2f} kW")
