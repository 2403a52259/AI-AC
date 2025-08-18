#!/usr/bin/env python3
"""
Biology Experiment: Cell Division Stages Simulation using Factorials
===============================================================

This script simulates how factorials can represent the exponential growth
of cell populations during division stages in a biology experiment.

In cell division, each generation doubles the population:
- Generation 0: 1 cell (2^0 = 1)
- Generation 1: 2 cells (2^1 = 2) 
- Generation 2: 4 cells (2^2 = 4)
- Generation 3: 8 cells (2^3 = 8)

The factorial n! represents the total number of possible arrangements
of n distinct objects, which can be related to cell division patterns.
"""

def calculate_factorial(n):
    """
    Calculate the factorial of a number n (n!)
    
    In biology context: This represents the total possible arrangements
    of n distinct cell division events or stages.
    
    Args:
        n (int): The number to calculate factorial for (must be non-negative)
    
    Returns:
        int: The factorial result n!
    
    Raises:
        ValueError: If n is negative
    """
    # Input validation: ensure n is non-negative
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base case: 0! = 1 (by mathematical definition)
    # In biology: represents the initial state before any division
    if n == 0:
        return 1
    
    # Base case: 1! = 1 (single cell state)
    # In biology: represents a single cell that hasn't divided yet
    if n == 1:
        return 1
    
    # Recursive calculation: n! = n × (n-1)!
    # In biology: each stage multiplies the previous stage's possibilities
    result = n * calculate_factorial(n - 1)
    
    return result


def simulate_cell_division_stages(max_generations):
    """
    Simulate cell division stages and show factorial relationships
    
    Args:
        max_generations (int): Maximum number of generations to simulate
    """
    print("🧬 CELL DIVISION STAGES SIMULATION 🧬")
    print("=" * 50)
    print("Generation | Cells | Factorial | Biological Meaning")
    print("-" * 50)
    
    for generation in range(max_generations + 1):
        # Calculate number of cells in this generation (2^generation)
        cells_in_generation = 2 ** generation
        
        # Calculate factorial for this generation
        factorial_result = calculate_factorial(generation)
        
        # Determine biological meaning based on generation
        if generation == 0:
            meaning = "Initial single cell"
        elif generation == 1:
            meaning = "First division - 2 daughter cells"
        elif generation == 2:
            meaning = "Second division - 4 granddaughter cells"
        elif generation == 3:
            meaning = "Third division - 8 great-granddaughter cells"
        else:
            meaning = f"{generation}th division - exponential growth"
        
        # Display the results
        print(f"{generation:^10} | {cells_in_generation:^5} | {factorial_result:^9} | {meaning}")
    
    print("-" * 50)


def analyze_factorial_growth():
    """
    Analyze how factorial growth compares to exponential cell growth
    """
    print("\n📊 FACTORIAL vs EXPONENTIAL GROWTH ANALYSIS 📊")
    print("=" * 60)
    print("Stage | Factorial | Exponential (2^n) | Ratio (Factorial/Exponential)")
    print("-" * 60)
    
    for stage in range(11):  # Analyze first 11 stages
        factorial_val = calculate_factorial(stage)
        exponential_val = 2 ** stage
        
        if exponential_val > 0:
            ratio = factorial_val / exponential_val
        else:
            ratio = float('inf')  # Division by zero case
        
        print(f"{stage:^5} | {factorial_val:^9} | {exponential_val:^16} | {ratio:^30.2f}")
    
    print("-" * 60)


def interactive_factorial_calculator():
    """
    Interactive calculator for users to explore factorial values
    """
    print("\n🔬 INTERACTIVE FACTORIAL CALCULATOR 🔬")
    print("=" * 40)
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter a number to calculate factorial (or 'quit' to exit): ")
            
            if user_input.lower() == 'quit':
                print("Thank you for exploring cell division mathematics! 🧬")
                break
            
            # Convert input to integer
            n = int(user_input)
            
            # Calculate factorial
            result = calculate_factorial(n)
            
            # Display result with biological context
            print(f"\n📈 RESULT: {n}! = {result}")
            
            if n <= 5:
                print("🔬 Biological interpretation:")
                if n == 0:
                    print("   - No cell divisions have occurred yet")
                elif n == 1:
                    print("   - Single cell state, no arrangements possible")
                elif n == 2:
                    print("   - Two cells can be arranged in 2 different ways")
                elif n == 3:
                    print("   - Three cells can be arranged in 6 different ways")
                elif n == 4:
                    print("   - Four cells can be arranged in 24 different ways")
                elif n == 5:
                    print("   - Five cells can be arranged in 120 different ways")
            else:
                print(f"🔬 Biological interpretation:")
                print(f"   - {n} distinct cell division events can be arranged in {result} different ways")
                print(f"   - This represents the complexity of {n}-stage division processes")
                
        except ValueError:
            print("❌ Please enter a valid integer number")
        except Exception as e:
            print(f"❌ Error: {e}")


def main():
    """
    Main function to run the biology experiment simulation
    """
    print("🧬 WELCOME TO THE CELL DIVISION FACTORIAL SIMULATION 🧬")
    print("This program demonstrates how factorials relate to biological processes")
    
    # Run the cell division simulation
    simulate_cell_division_stages(8)
    
    # Analyze factorial vs exponential growth
    analyze_factorial_growth()
    
    # Run interactive calculator
    interactive_factorial_calculator()


# Run the main program if this script is executed directly
if __name__ == "__main__":
    main()
