# Hamouda Informational Gravity Model (HIGM) - Core Calculator
# Developed by Prof. Dr. Samir Ahmed Hamouda

def calculate_higm_boost(mass_density):
    """
    Computes the HIGM Information Entropy and the resulting gravitational boost factor.
    Core Law: Information Entropy (S) is inversely proportional to Mass Density (rho).
    """
    if mass_density <= 0:
        return "Error: Mass density must be greater than zero."
        
    # 1. Calculate Inverse Entropy Proportionality (S = 1 / rho)
    information_entropy = 1.0 / mass_density
    
    # 2. Apply the Standard HIGM 9.05% Shannon Correction Factor (0.0905)
    higm_correction_factor = 0.0905
    
    # g_HIGM = g_GR * (1 + beta)
    total_gravitational_multiplier = 1.0 + higm_correction_factor
    
    print("--- HIGM MODEL CALCULATION RESULTS ---")
    print(f"Input Mass Density (rho): {mass_density} kg/m^3")
    print(f"Calculated Vacuo-Informational Entropy (S): {information_entropy:.4f}")
    print(f"Standard Shannon Boost Factor (beta): {higm_correction_factor * 100}%")
    print(f"Total Gravitational Multiplier: {total_gravitational_multiplier}x")
    print("--------------------------------------")
    
    return total_gravitational_multiplier

# Run a sample test using a low-density cosmic void parameter
sample_density = 0.15
calculate_higm_boost(sample_density)

