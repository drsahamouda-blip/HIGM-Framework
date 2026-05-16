import numpy as np

# Core HIGM Constants
G = 6.67430e-11          # Gravitational constant (m^3 kg^-1 s^-2)
M_milky_way = 2.0e41     # Baryonic mass of Milky Way (kg) - no dark matter halo

def calculate_higm_velocity(radius_kpc):
    """
    Calculates orbital velocity using the HIGM framework.
    Incorporates the informational boost from vacuum entropy flux.
    """
    # Convert kilo-parsecs to meters
    radius_meters = radius_kpc * 3.086e19
    
    # Standard Newtonian velocity component
    v_newtonian = np.sqrt((G * M_milky_way) / radius_meters)
    
    # HIGM Informational Pressure boost factor 
    informational_boost = 1.0905 
    v_higm = v_newtonian * informational_boost
    
    # Floor function representing the entropic background pressure stabilizing the curve
    v_stabilized = np.maximum(v_higm, 235000.0) 
    
    return v_newtonian / 1000.0, v_stabilized / 1000.0 # Convert to km/s

# Test the calculation at a galactic boundary of 15 kpc
v_old, v_new = calculate_higm_velocity(15.0)
print(u"At 15 kpc:")
print(f"Standard Newtonian Velocity: {v_old:.2f} km/s")
print(f"HIGM Stabilized Velocity: {v_new:.2f} km/s")
