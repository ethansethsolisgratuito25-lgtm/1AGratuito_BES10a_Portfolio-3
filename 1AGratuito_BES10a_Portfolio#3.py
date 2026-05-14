# Portfolio 3: Functions
# Course: BES10a
# Student: Ethan Seth S. Gratuito
# Project: Analytical Chemistry Lab Assistant

def calculate_moles(mass, molar_mass):
    # Calculates moles given mass in grams and molar mass.
    moles = mass / molar_mass
    return moles

def calculate_molarity(moles, volume_liters):
    # Calculates molarity (M) given moles and volume in liters.
    molarity = moles / volume_liters
    return molarity

print("--- Lab 4: Titration Data Cruncher ---")
print("Data processing for Ethan, Dylan, and Ashley...\n")

try:
    # Gathering the raw laboratory data
    sample_mass = float(input("Enter the mass of the solute (in grams): "))
    sample_molar_mass = float(input("Enter the molar mass of the solute (g/mol): "))
    solution_volume = float(input("Enter the volume of the solution (in liters): "))

    # Passing the inputs into our custom functions
    calculated_moles = calculate_moles(sample_mass, sample_molar_mass)
    final_molarity = calculate_molarity(calculated_moles, solution_volume)

    # Outputting the results, formatting to 4 decimal places for precision
    print("\n--- Results ---")
    print(f"Moles of solute: {calculated_moles:.4f} mol")
    print(f"Molarity of solution: {final_molarity:.4f} M")

except ValueError:
    print("\nLab Error: Please enter valid numeric data for the measurements.")
    print("Action Required: Check your inputs. We don't want to restart the whole calculation.")
